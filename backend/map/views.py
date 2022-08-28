from django.db.models import F
from django.utils.decorators import method_decorator
from django_filters import rest_framework as filters

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from map import mixins, serializers
from map.filters import ArcFilterSet
from map.models import Node, Arc
from map.pagination import (
    HateoasGeoJsonPagination,
    HateoasGeoJsonPaginatorInspector,
)
from map.schema import (
    node_list_schema,
    arc_optimal_schema,
)


@method_decorator(name='get', decorator=swagger_auto_schema(
    responses={
        200: openapi.Response(
            description='노드 리스트를 GeoJson 형태로 반환',
            schema=node_list_schema,
        )
    }
))
class NodeListView(generics.ListAPIView):
    queryset = Node.objects.all()
    serializer_class = serializers.NodeListSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter('level', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, enum=[1, 2, 3],
                          description='경로 배리어프리 수준')
    ],
    paginator_inspectors=[HateoasGeoJsonPaginatorInspector],
))
class ArcListView(generics.ListAPIView):
    queryset = Arc.objects.all()
    serializer_class = serializers.ArcListSerializer
    pagination_class = HateoasGeoJsonPagination
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ArcFilterSet

    def get_queryset(self):
        level = self.request.query_params.get('level')
        if level and level not in {'1', '2', '3'}:
            raise ValidationError({'level': '1, 2, 3 중 한 값이여야 합니다.'})
        return super().get_queryset()


class ArcOptimalView(mixins.OptimalPathMixin,
                     generics.GenericAPIView):
    serializer_class = serializers.ArcOptimalSerializer

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description='노드 좌표(경도, 위도)가 연결된 LineString 형태로 최적 경로 반환',
                schema=arc_optimal_schema,
            )
        }
    )
    def post(self, request, *args, **kwargs):
        return self.optimal(request, *args, **kwargs)
