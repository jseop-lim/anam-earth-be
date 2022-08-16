from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.inspectors import PaginatorInspector


class HateoasGeoJsonPagination(pagination.LimitOffsetPagination):
    limit_query_param = 'per_page'
    offset_query_param = 'page'

    @staticmethod
    def get_link_data(url, rel):
        return OrderedDict([
            ('rel', rel),
            ('method', 'GET' if url else None),
            ('link', url),
        ])

    def get_paginated_response(self, data):
        links = [
            (self.get_previous_link(), 'prev'),
            (self.get_next_link(), 'next')
        ]
        links_header = []
        links_data = []
        for url, rel in links:
            if url is not None:
                links_header.append(f'<{url}>; rel="{rel}"')
            links_data.append(self.get_link_data(url, rel))

        return Response(
            OrderedDict([
                ('type', 'FeatureCollection'),
                ('features', data['features']),
                ('links', links_data)
            ]),
            headers={'Link': ', '.join(links_header)} if links_header else {}
        )


class HateoasGeoJsonPaginatorInspector(PaginatorInspector):

    def get_paginated_response(self, paginator, response_schema):
        assert response_schema.type == openapi.TYPE_ARRAY, "array return expected for paged response"

        if not isinstance(paginator, HateoasGeoJsonPagination):
            return None

        return openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=OrderedDict((
                ('type', openapi.Schema(type=openapi.TYPE_STRING)),
                ('features', response_schema),
                ('links', openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        title='Link',
                        description='인접 페이지 링크',
                        type=openapi.TYPE_OBJECT,
                        properties=OrderedDict((
                            ('rel', openapi.Schema(type=openapi.TYPE_STRING, enum=['prev', 'next'])),
                            ('method', openapi.Schema(type=openapi.TYPE_STRING, enum=['GET'])),
                            ('link', openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, x_nullable=True)),
                        ))
                    ),
                )),
            )),
            required=['features']
        )
