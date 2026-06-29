from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import (State, District,Tehsil,Village,)
from .serializers import (StateSerializer,DistrictSerializer,TehsilSerializer,VillageSerializer,)
from .services import (StateService,DistrictService,TehsilService,VillageService,)

class StateListAPIView(generics.ListAPIView):
    serializer_class = StateSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return StateService.get_all()
class StateRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = StateSerializer
    permission_classes = [AllowAny]
    lookup_field = "pk"

    def get_queryset(self):
        return State.objects.filter(is_active=True)
class DistrictListAPIView(generics.ListAPIView):
    serializer_class = DistrictSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        state_id = self.request.query_params.get("state")
        if state_id:
            return DistrictService.get_by_state(state_id)
        return DistrictService.get_all()
class DistrictRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DistrictSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return District.objects.filter(is_active=True)

class TehsilListAPIView(generics.ListAPIView):
    serializer_class = TehsilSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        district_id = self.request.query_params.get("district")
        if district_id:
            return TehsilService.get_by_district(district_id)
        return TehsilService.get_all()
class TehsilRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TehsilSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Tehsil.objects.filter(is_active=True)
class VillageListAPIView(generics.ListAPIView):
    serializer_class = VillageSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        tehsil_id = self.request.query_params.get("tehsil")
        search = self.request.query_params.get("search")
        if search:
            return VillageService.search(search)
        if tehsil_id:
            return VillageService.get_by_tehsil(tehsil_id)
        return VillageService.get_all()


class VillageRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = VillageSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Village.objects.filter(is_active=True)