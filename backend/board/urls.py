from django.urls import path, include
from rest_framework.routers import DefaultRouter
from board import views


router = DefaultRouter(trailing_slash=False)
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
