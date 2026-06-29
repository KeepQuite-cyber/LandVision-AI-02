from django.contrib import admin
from .models import (
    Owner,
    Plot,
)


# ==========================================================
# Common Admin Actions
# ==========================================================

@admin.action(description="Mark selected records as Active")
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Mark selected records as Inactive")
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


# ==========================================================
# Owner Admin
# ==========================================================

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "father_name",
        "mobile",
        "email",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "father_name",
        "mobile",
        "email",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    actions = (
        make_active,
        make_inactive,
    )

    list_per_page = 25

    fieldsets = (

        ("Owner Information", {
            "fields": (
                "name",
                "father_name",
            )
        }),

        ("Contact Details", {
            "fields": (
                "mobile",
                "email",
            )
        }),

        ("Status", {
            "fields": (
                "is_active",
            )
        }),

        ("Timestamps", {
            "classes": (
                "collapse",
            ),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )


# ==========================================================
# Plot Admin
# ==========================================================

@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "plot_number",
        "owner",
        "village",
        "land_use",
        "area",
        "is_active",
    )

    search_fields = (
        "plot_number",
        "owner__name",
        "owner__father_name",
        "village__name",
        "village__tehsil__name",
        "village__tehsil__district__name",
        "village__tehsil__district__state__name",
    )

    list_filter = (
        "land_use",
        "village",
        "is_active",
    )

    ordering = (
        "plot_number",
    )

    autocomplete_fields = (
        "owner",
        "village",
    )

    list_select_related = (
        "owner",
        "village",
        "village__tehsil",
        "village__tehsil__district",
        "village__tehsil__district__state",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    actions = (
        make_active,
        make_inactive,
    )

    list_per_page = 25

    fieldsets = (

        ("Plot Information", {
            "fields": (
                "plot_number",
                "village",
                "owner",
            )
        }),

        ("Land Information", {
            "fields": (
                "area",
                "land_use",
            )
        }),

        ("Polygon", {
            "fields": (
                "polygon",
            )
        }),

        ("Remarks", {
            "fields": (
                "remarks",
            )
        }),

        ("Status", {
            "fields": (
                "is_active",
            )
        }),

        ("Timestamps", {
            "classes": (
                "collapse",
            ),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )