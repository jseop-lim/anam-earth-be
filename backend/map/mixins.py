from django.db.models import F, Q, Case, When
from django.contrib.gis.geos import LineString

from rest_framework import status
from rest_framework.response import Response

import networkx as nx

from map.models import Arc, Node
from map.serializers import GeometrySerializer


class BasePathMixin:

    def path(self, request, *args, **kwargs):
        request_serializer = self.get_serializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        response_serializer = self.transform_serializer(request_serializer)
        response_serializer.is_valid(raise_exception=True)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def perform_optimal(self, start_node, end_node, ebunch_to_add):
        graph = nx.Graph()
        graph.add_weighted_edges_from(ebunch_to_add)
        optimal_path = nx.shortest_path(
            graph,
            source=start_node,
            target=end_node,
            weight='weight',
            method='dijkstra'
        )
        return optimal_path

    def get_arc_queryset(self):
        return NotImplemented

    def transform_serializer(self, serializer):
        start_node = serializer.data['start_node']
        end_node = serializer.data['end_node']
        arcs_values = self.get_arc_queryset(
        ).values_list(
            'start_node', 'end_node', 'weight'
        )
        optimal_nodes_id = self.perform_optimal(start_node, end_node, arcs_values)

        preserved = Case(*[When(pk=pk, then=order) for order, pk in enumerate(optimal_nodes_id)])
        optimal_nodes_point = Node.objects.filter(
            pk__in=optimal_nodes_id
        ).order_by(preserved).values_list('point', flat=True)

        linestring = LineString(list(optimal_nodes_point))
        return GeometrySerializer(data={'geometry': linestring})


class OptimalPathMixin(BasePathMixin):

    def _get_weight_coefficient(self, level):
        return 2.5 ** (level if level > 1 else 0)

    def get_arc_queryset(self):
        return Arc.objects.annotate(
            gradient=F('vertical_distance') / F('horizontal_distance'),
            weight_coeff=Case(
                When(Q(gradient__gt=0.08) | Q(is_stair=True) | Q(is_step=True), then=self._get_weight_coefficient(3)),
                When(Q(gradient__gt=0.055) & Q(quality='하'), then=self._get_weight_coefficient(2)),
                default=self._get_weight_coefficient(1),
            ),
            weight=F('horizontal_distance') * F('weight_coeff'),
        )


class ShortestPathMixin(BasePathMixin):

    def get_arc_queryset(self):
        return Arc.objects.annotate(
            weight=F('horizontal_distance')
        )
