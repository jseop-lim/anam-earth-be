from collections import OrderedDict

from django.contrib.gis.geos import LineString, Point
from django.contrib.gis.measure import D

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    GeometryField,
    GeometrySerializerMethodField,
)

from map.models import Arc, Node
from map.functions import DistanceSphere


class NodeListSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Node
        fields = []  # 속도를 위해 비움
        geo_field = 'point'
        id_field = False


class ArcListSerializer(GeoFeatureModelSerializer):
    linestrings = GeometrySerializerMethodField()

    class Meta:
        model = Arc
        fields = ['id', 'level']  # property 필드도 포함 가능
        geo_field = 'linestrings'  # fields 리스트에 미포함 가능
        id_field = False

    def get_linestrings(self, obj: Arc):
        return LineString(obj.start_node.point, obj.end_node.point)


class CoordinateListField(serializers.ListField):
    child = serializers.FloatField()
    allow_empty = False
    min_length = 2
    max_length = 2

    def run_child_validation(self, data):
        result = super().run_child_validation(data)
        errors = OrderedDict()

        longitude, latitude = float(data[0]), float(data[1])
        if not -180 <= longitude <= 180:
            errors[0] = ['경도 범위 오류입니다.']
        if not -90 <= latitude <= 90:
            errors[1] = ['위도 범위 오류입니다.']

        if not errors:
            return result
        raise ValidationError(errors)


class ArcPathSerializer(serializers.Serializer):
    start_coordinate = CoordinateListField(write_only=True)
    end_coordinate = CoordinateListField(write_only=True)
    start_node = serializers.SerializerMethodField()
    end_node = serializers.SerializerMethodField()

    @staticmethod
    def get_nearest_node(longitude, latitude):
        point = Point(longitude, latitude, srid=4326)
        node = Node.objects.annotate(
            distance=DistanceSphere('point', point)
        ).filter(
            distance__lte=D(mi=500).mi
        ).order_by('distance').first()
        return node

    def get_start_node(self, obj):
        start_node = self.get_nearest_node(*obj['start_coordinate'])
        if start_node is None:
            raise ValidationError({'start_coordinate': '가까운 출발 노드가 없습니다.'})
        return start_node.id

    def get_end_node(self, obj):
        end_node = self.get_nearest_node(*obj['end_coordinate'])
        if end_node is None:
            raise ValidationError({'end_coordinate': '가까운 도착 노드가 없습니다.'})
        return end_node.id


class GeometrySerializer(serializers.Serializer):
    geometry = GeometryField()

    class Meta:
        geo_field = 'geometry'
