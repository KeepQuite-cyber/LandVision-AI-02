from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/",include("village.urls"),),
    path("api/v1/",include("plot.urls"),),
    path("api/v1/",include("ai.urls"),),
]