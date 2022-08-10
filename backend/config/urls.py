from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


board_schema_view = get_schema_view(
    openapi.Info(
        title='Anam-Earth Board API',
        default_version='develop',
        description='안암어스 게시판 API',
        contact=openapi.Contact(email="jseoplim@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    patterns=[
        path('board/', include('board.urls'))  # url_pattern 의존
    ]
)

map_schema_view = get_schema_view(
    openapi.Info(
        title='Anam-Earth Map API',
        default_version='develop',
        description='안암어스 지도 API',
        contact=openapi.Contact(email="jseoplim@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    patterns=[
        path('map/', include('map.urls'))  # url_pattern 의존
    ]
)


urlpatterns = [
    path('board/', include('board.urls')),
    path('board/swagger', board_schema_view.with_ui('swagger', cache_timeout=0), name='board-schema-swagger-ui'),
    path('map/', include('map.urls')),
    path('map/swagger', map_schema_view.with_ui('swagger', cache_timeout=0), name='map-schema-swagger-ui'),
]
