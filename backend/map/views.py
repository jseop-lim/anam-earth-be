from django.db.models import F
from django.utils.decorators import method_decorator
from django_filters import rest_framework as filters

from rest_framework import generics
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from map import serializers
from map.filters import ArcFilterSet
from map.models import Arc
from map.pagination import HateoasGeoJsonPagination, HateoasGeoJsonPaginatorInspector


@method_decorator(name='get', decorator=swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter('level', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, enum=[1, 2, 3],
                          description='경로 배리어프리 수준')
    ],
    paginator_inspectors=[HateoasGeoJsonPaginatorInspector],
))
class ArcListView(generics.ListAPIView):
    queryset = Arc.objects.filter(start_node_id__lt=F('end_node_id'))
    serializer_class = serializers.ArcListSerializer
    pagination_class = HateoasGeoJsonPagination
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ArcFilterSet
