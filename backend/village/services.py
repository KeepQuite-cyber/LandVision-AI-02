from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import (
    State,
    District,
    Tehsil,
    Village,
)


class BaseService:
    """
    Base service containing common reusable methods.
    """

    @staticmethod
    def active(queryset):
        """
        Return only active records.
        """
        return queryset.filter(is_active=True)

    @staticmethod
    def get_object(queryset, **filters):
        """
        Return a single object or raise 404.
        """
        return get_object_or_404(queryset, **filters)


# ==========================================================
# State Service
# ==========================================================

class StateService(BaseService):

    queryset = State.objects.all()

    @classmethod
    def get_all(cls):
        return (
            cls.active(cls.queryset)
            .order_by("name")
        )

    @classmethod
    def get(cls, state_id):
        return cls.get_object(
            cls.queryset,
            pk=state_id,
            is_active=True
        )


# ==========================================================
# District Service
# ==========================================================

class DistrictService(BaseService):

    queryset = District.objects.select_related(
        "state"
    )

    @classmethod
    def get_all(cls):
        return (
            cls.active(cls.queryset)
            .order_by("name")
        )

    @classmethod
    def get(cls, district_id):
        return cls.get_object(
            cls.queryset,
            pk=district_id,
            is_active=True
        )

    @classmethod
    def get_by_state(cls, state_id):
        return (
            cls.active(cls.queryset)
            .filter(state_id=state_id)
            .order_by("name")
        )


# ==========================================================
# Tehsil Service
# ==========================================================

class TehsilService(BaseService):

    queryset = Tehsil.objects.select_related(
        "district",
        "district__state"
    )

    @classmethod
    def get_all(cls):
        return (
            cls.active(cls.queryset)
            .order_by("name")
        )

    @classmethod
    def get(cls, tehsil_id):
        return cls.get_object(
            cls.queryset,
            pk=tehsil_id,
            is_active=True
        )

    @classmethod
    def get_by_district(cls, district_id):
        return (
            cls.active(cls.queryset)
            .filter(district_id=district_id)
            .order_by("name")
        )


# ==========================================================
# Village Service
# ==========================================================

class VillageService(BaseService):

    queryset = Village.objects.select_related(
        "tehsil",
        "tehsil__district",
        "tehsil__district__state",
    )

    @classmethod
    def get_all(cls):
        return (
            cls.active(cls.queryset)
            .order_by("name")
        )

    @classmethod
    def get(cls, village_id):
        return cls.get_object(
            cls.queryset,
            pk=village_id,
            is_active=True
        )

    @classmethod
    def get_by_tehsil(cls, tehsil_id):
        return (
            cls.active(cls.queryset)
            .filter(tehsil_id=tehsil_id)
            .order_by("name")
        )

    @classmethod
    def search(cls, keyword):
        """
        Search village by multiple fields.
        """

        return (
            cls.active(cls.queryset)
            .filter(
                Q(name__icontains=keyword)
                | Q(village_code__icontains=keyword)
                | Q(gis_code__icontains=keyword)
                | Q(pincode__icontains=keyword)
                | Q(tehsil__name__icontains=keyword)
                | Q(tehsil__district__name__icontains=keyword)
                | Q(tehsil__district__state__name__icontains=keyword)
            )
            .distinct()
            .order_by("name")
        )