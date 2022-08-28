from django.db.models import F, Q, Case, When
from django.contrib.gis.geos import LineString

from rest_framework import status
from rest_framework.response import Response

import networkx as nx

from map.models import Arc, Node
from map.serializers import OptimalPathSerializer


class OptimalPathMixin:

    def optimal(self, request, *args, **kwargs):
        request_serializer = self.get_serializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        response_serializer = self.transform_serializer(request_serializer)
        response_serializer.is_valid(raise_exception=True)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def get_weight_coefficient(self, level):
        return 2.5 ** (level if level > 1 else 0)

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

    def transform_serializer(self, serializer):
        start_node = serializer.data['start_node']
        end_node = serializer.data['end_node']
        arcs_values = Arc.objects.annotate(
            gradient=F('vertical_distance') / F('horizontal_distance'),
            weight_coeff=Case(
                When(Q(gradient__gt=0.08) | Q(is_stair=True) | Q(is_step=True), then=self.get_weight_coefficient(3)),
                When(Q(gradient__gt=0.055) & Q(quality='하'), then=self.get_weight_coefficient(2)),
                default=self.get_weight_coefficient(1),
            ),
            weight=F('horizontal_distance') * F('weight_coeff')
        ).values_list(
            'start_node', 'end_node', 'weight'
        )
        optimal_nodes_id = self.perform_optimal(start_node, end_node, arcs_values)

        preserved = Case(*[When(pk=pk, then=order) for order, pk in enumerate(optimal_nodes_id)])
        optimal_nodes_point = Node.objects.filter(
            pk__in=optimal_nodes_id
        ).order_by(preserved).values_list('point', flat=True)

        linestring = LineString(list(optimal_nodes_point))
        return OptimalPathSerializer(data={'geometry': linestring})
