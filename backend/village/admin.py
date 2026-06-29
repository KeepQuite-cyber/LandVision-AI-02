from django.contrib import admin
from .models import State, District, Tehsil, Village


@admin.action(description="Mark selected records as Active")
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Mark selected records as Inactive")
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("id","name","code","is_active","created_at",)
    search_fields = ("name","code",)
    list_filter = ("is_active",)
    ordering = ("name",)
    readonly_fields = ("created_at","updated_at",)
    actions = (make_active,make_inactive,)
    list_per_page = 20

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ( "id","name","state","code","is_active",)
    search_fields = ("name","code","state__name",)
    list_filter = ("state","is_active",)
    autocomplete_fields = ("state",)
    list_select_related = ("state",)
    readonly_fields = ("created_at","updated_at",)
    ordering = ("name",)
    actions = (make_active,make_inactive,)
    list_per_page = 20
@admin.register(Tehsil)
class TehsilAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "district", "code", "is_active",)
    search_fields = ("name", "district__name", "district__state__name",)
    list_filter = ("district","is_active",)
    autocomplete_fields = ("district",)
    list_select_related = ("district",)
    readonly_fields = ("created_at","updated_at",)
    ordering = ("name",)
    actions = (make_active,make_inactive,)
    list_per_page = 20
@admin.register(Village)
class VillageAdmin(admin.ModelAdmin): 
    list_display = ("id","name","tehsil","village_code","gis_code","is_active",)
    search_fields = ("name","village_code","gis_code", "tehsil__name", "tehsil__district__name","tehsil__district__state__name",)
    list_filter = ("tehsil","is_active",)
    autocomplete_fields = ( "tehsil",)
    list_select_related = ("tehsil", "tehsil__district","tehsil__district__state",)
    readonly_fields = ("created_at", "updated_at",)
    ordering = ( "name",)
    actions = ( make_active, make_inactive,)
    list_per_page = 20
    fieldsets = (("Village Information", {"fields": ( "name", "tehsil", "village_code", "gis_code",)}),("Location", {"fields": ("latitude","longitude","pincode", )}),("Status", {
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