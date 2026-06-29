from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import ( Owner,Plot,)
from .serializers import (OwnerSerializer,PlotListSerializer,PlotDetailSerializer,PlotMapSerializer,)
from .services import (OwnerService,PlotService,)
class OwnerListAPIView(generics.ListAPIView):
    """
    List all owners.
    """
    serializer_class = OwnerSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["name","father_name","mobile","email",]
    ordering_fields = ["name",]
    ordering = ["name",]
    def get_queryset(self):
        return OwnerService.get_all()
class OwnerDetailAPIView(generics.RetrieveAPIView): 
    serializer_class = OwnerSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return OwnerService.get_all()

class PlotListAPIView(generics.ListAPIView):
    serializer_class = PlotListSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,]

    filterset_fields = ["land_use","village","owner",]
    search_fields = ["plot_number","owner__name","owner__father_name","village__name","village__tehsil__name","village__tehsil__district__name",]

    ordering_fields = [
        "plot_number",
        "area",
    ]

    ordering = [
        "plot_number",
    ]

    def get_queryset(self):
        return PlotService.get_all()


# ==========================================================
# Plot Detail View
# ==========================================================

class PlotDetailAPIView(generics.RetrieveAPIView):
    """
    Retrieve single plot.
    """

    serializer_class = PlotDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return PlotService.get_all()


# ==========================================================
# Plot Map View
# ==========================================================

class PlotMapAPIView(generics.ListAPIView):
    """
    Returns lightweight plot data for Leaflet.
    """

    serializer_class = PlotMapSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):

        village_id = self.request.query_params.get(
            "village"
        )

        return PlotService.map_data(
            village_id=village_id
        )