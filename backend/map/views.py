from django.db.models import F
from django.utils.decorators import method_decorator

from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema

from map import serializers
from map.models import Arc
from map.pagination import HateoasGeoJsonPagination, HateoasGeoJsonPaginatorInspector


@method_decorator(name='get', decorator=swagger_auto_schema(
    paginator_inspectors=[HateoasGeoJsonPaginatorInspector],
))
class ArcListView(generics.ListAPIView):
    queryset = Arc.objects.filter(start_node_id__lt=F('end_node_id'))
    serializer_class = serializers.ArcListSerializer
    pagination_class = HateoasGeoJsonPagination
