from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import (Owner,Plot,)

# ==========================================================
# Base Service
# ==========================================================
class BaseService:
    """
    Base service containing common reusable methods.
    """
    @staticmethod
    def active(queryset):
        return queryset.filter(is_active=True)

    @staticmethod
    def inactive(queryset):
        return queryset.filter(is_active=False)

    @staticmethod
    def get_object(queryset, **filters):
        return get_object_or_404(queryset, **filters)


# ==========================================================
# Owner Service
# ==========================================================
class OwnerService(BaseService):
    queryset = Owner.objects.all()
    @classmethod
    def get_all(cls):
        return ( cls.active(cls.queryset).order_by("name"))

    @classmethod
    def get(cls, owner_id):
        return cls.get_object(cls.queryset,pk=owner_id,is_active=True,)

    @classmethod
    def search(cls, keyword):
        return (cls.active(cls.queryset).filter(
                Q(name__icontains=keyword)
                | Q(father_name__icontains=keyword)
                | Q(mobile__icontains=keyword)
                | Q(email__icontains=keyword)
            )
            .distinct()
            .order_by("name")
        )

# ==========================================================
# Plot Service
# ==========================================================
class PlotService(BaseService):
    queryset = Plot.objects.select_related("owner","village","village__tehsil","village__tehsil__district","village__tehsil__district__state",)

    @classmethod
    def get_all(cls):
        return (cls.active(cls.queryset).order_by("plot_number"))

    @classmethod
    def get(cls, plot_id):
        return cls.get_object(cls.queryset,pk=plot_id,is_active=True,)

    @classmethod
    def get_by_plot_number(cls, plot_number):
        return (cls.active(cls.queryset).filter(plot_number=plot_number).order_by("plot_number"))

    @classmethod
    def get_by_owner(cls, owner_id):
        return ( cls.active(cls.queryset) .filter(owner_id=owner_id) .order_by("plot_number"))
    
    @classmethod
    def get_by_village(cls, village_id):
        return (cls.active(cls.queryset).filter(village_id=village_id).order_by("plot_number"))

    @classmethod
    def get_by_land_use(cls, land_use):
        return (cls.active(cls.queryset).filter(land_use=land_use).order_by("plot_number"))

    @classmethod
    def search(cls, keyword):
        return (
            cls.active(cls.queryset)
            .filter(
                Q(plot_number__icontains=keyword)
                | Q(owner__name__icontains=keyword)
                | Q(owner__father_name__icontains=keyword)
                | Q(village__name__icontains=keyword)
                | Q(village__village_code__icontains=keyword)
                | Q(village__gis_code__icontains=keyword)
                | Q(village__tehsil__name__icontains=keyword)
                | Q(village__tehsil__district__name__icontains=keyword)
                | Q(village__tehsil__district__state__name__icontains=keyword)
            )
            .distinct()
            .order_by("plot_number")
        )

    @classmethod
    def map_data(cls, village_id=None):
        queryset = cls.active(
        Plot.objects.all()
        )
        if village_id:
            queryset = queryset.filter(village_id=village_id)
        return queryset.only("id","plot_number","polygon","land_use",)

    @classmethod
    def statistics(cls):
        queryset = cls.active(cls.queryset)
        return {
            "total_plots": queryset.count(),
            "agriculture": queryset.filter(
                land_use="Agriculture"
            ).count(),
            "residential": queryset.filter(
                land_use="Residential"
            ).count(),
            "commercial": queryset.filter(
                land_use="Commercial"
            ).count(),
            "industrial": queryset.filter(
                land_use="Industrial"
            ).count(),
            "government": queryset.filter(
                land_use="Government"
            ).count(),
            "others": queryset.filter(
                land_use="Others"
            ).count(),
        }