from django.urls import path

from .views import (StateListAPIView,StateRetrieveAPIView,DistrictListAPIView,DistrictRetrieveAPIView,TehsilListAPIView,TehsilRetrieveAPIView,VillageListAPIView,VillageRetrieveAPIView,)

app_name = "village"
urlpatterns = [
    path ("states/",StateListAPIView.as_view(),name="state-list",),
    path("states/<int:pk>/",StateRetrieveAPIView.as_view(),name="state-detail",),
    path("districts/",DistrictListAPIView.as_view(),name="district-list",),
    path( "districts/<int:pk>/", DistrictRetrieveAPIView.as_view(), name="district-detail",),
    path("tehsils/",TehsilListAPIView.as_view(), name="tehsil-list",),
    path( "tehsils/<int:pk>/",TehsilRetrieveAPIView.as_view(),name="tehsil-detail",),
    path( "villages/", VillageListAPIView.as_view(), name="village-list", ),
    path("villages/<int:pk>/", VillageRetrieveAPIView.as_view(),name="village-detail",),
]