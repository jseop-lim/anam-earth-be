from django.contrib.gis.db.models import PointField, LineStringField

from rest_framework_gis.schema import GeoFeatureAutoSchema
from drf_yasg import openapi


node_list_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'type': openapi.Schema(type=openapi.TYPE_STRING, enum=['FeatureCollection']),
        'features': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'type': openapi.Schema(type=openapi.TYPE_STRING, enum=['Feature']),
                    'geometry': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties=GeoFeatureAutoSchema.GEO_FIELD_TO_SCHEMA[PointField]
                    )
                }
            )
        )
    }
)

arc_path_schema = openapi.Schema(
    title='geometry',
    type=openapi.TYPE_OBJECT,
    properties=GeoFeatureAutoSchema.GEO_FIELD_TO_SCHEMA[LineStringField]
)
