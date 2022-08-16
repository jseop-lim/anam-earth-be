from django.contrib.gis.geos import LineString

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField

from map.models import Arc


class ArcListSerializer(GeoFeatureModelSerializer):
    line_strings = GeometrySerializerMethodField()

    class Meta:
        model = Arc
        fields = ['id', 'level']  # property 필드도 포함 가능
        geo_field = 'line_strings'  # fields 리스트에 미포함 가능

    def get_line_strings(self, obj: Arc):
        return LineString(obj.start_node.point, obj.end_node.point)
