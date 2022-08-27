from django.urls import path

from map import views


urlpatterns = [
    path('arcs', views.ArcListView.as_view(), name='arc-list'),
    path('arcs/optimal', views.ArcOptimalView.as_view(), name='arc-optimal'),
]
