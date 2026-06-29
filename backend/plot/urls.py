from django.urls import path
from .views import (OwnerListAPIView,OwnerDetailAPIView,PlotListAPIView,PlotDetailAPIView,PlotMapAPIView,)

app_name = "plot"
urlpatterns = [
    path("owners/",OwnerListAPIView.as_view(),name="owner-list",),
    path("owners/<int:pk>/",OwnerDetailAPIView.as_view(),name="owner-detail",),
    path("plots/",PlotListAPIView.as_view(),name="plot-list",),
    path("plots/<int:pk>/",PlotDetailAPIView.as_view(),name="plot-detail",),
    path( "plots/map/", PlotMapAPIView.as_view(), name="plot-map",),
]