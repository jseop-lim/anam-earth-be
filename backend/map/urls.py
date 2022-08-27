from django.urls import path

from map import views


urlpatterns = [
    path('nodes', views.NodeListView.as_view(), name='node-list'),
    path('arcs', views.ArcListView.as_view(), name='arc-list'),
    path('arcs/optimal', views.ArcOptimalView.as_view(), name='arc-optimal'),
]
