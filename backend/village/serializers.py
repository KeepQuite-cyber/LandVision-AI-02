from rest_framework import serializers
from .models import (State, District, Tehsil, Village,)
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ["id","name","code",]

class DistrictSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)
    class Meta:
        model = District
        fields = ["id","name","code","state",]

class TehsilSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    class Meta:
        model = Tehsil
        fields = ["id","name","code","district",]


class VillageSerializer(serializers.ModelSerializer):
    tehsil = TehsilSerializer(read_only=True)
    class Meta:
        model = Village
        fields = ["id","name","village_code","gis_code","pincode","latitude","longitude","tehsil",]