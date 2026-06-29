from rest_framework import serializers
from village.serializers import VillageSerializer
from .models import (Owner,Plot,)
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ("id","name","father_name","mobile","email",)
class PlotListSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source="owner.name",read_only=True,)
    village_name = serializers.CharField(source="village.name",read_only=True,)
    class Meta:
        model = Plot
        fields = ("id", "plot_number","owner_name","village_name","area","land_use",)
class PlotDetailSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    village = VillageSerializer(read_only=True)
    class Meta:
        model = Plot
        fields = ("id", "plot_number", "area", "land_use", "polygon", "remarks", "owner", "village",)
class PlotMapSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source="owner.name",read_only=True,)
    village_name = serializers.CharField(source="village.name",read_only=True,)
    tehsil_name = serializers.CharField( source="village.tehsil.name", read_only=True,)
    district_name = serializers.CharField(source="village.tehsil.district.name",read_only=True,)
    state_name = serializers.CharField(source="village.tehsil.district.state.name",read_only=True,)
    class Meta:
        model = Plot
        fields = ("id","plot_number","area","land_use","polygon","remarks","owner_name","village_name","tehsil_name","district_name","state_name",)
class PlotCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ( "village","owner","plot_number","area","land_use","polygon","remarks",)