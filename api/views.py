from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer
from django.db.models import F, FloatField
from django.db.models.functions import ACos, Cos, Radians, Sin, Sqrt
from .models import Doctor, Specialization
from .serializers import (
    DoctorSerializer,
    SpecializationSerializer,
    DoctorsOfSpecializationSerializer,
)


class DoctorListByLocationView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        queryset = Doctor.objects.all()
        try:
            latitude = float(self.request.query_params.get("latitude"))
            longitude = float(self.request.query_params.get("longitude"))
        except (TypeError, ValueError):
            raise ValueError("Valid latitude and longitude are required.")

        # Haversine formula to calculate distance in kilometers
        lat_rad = Radians(F("latitude"))
        lon_rad = Radians(F("longitude"))
        user_lat_rad = Radians(latitude)
        user_lon_rad = Radians(longitude)

        distance_expr = (
            6371
            * 2
            * ACos(
                Cos(user_lat_rad) * Cos(lat_rad) * Cos(lon_rad - user_lon_rad)
                + Sin(user_lat_rad) * Sin(lat_rad)
            )
        )

        # Annotate queryset with distance and filter by a 5 km radius
        queryset = (
            queryset.annotate(distance=distance_expr)
            .filter(distance__lte=5)
            .order_by("distance")
        )
        return queryset


class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class SpecializationListCreateView(generics.ListCreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class SpecializationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class DoctorListBySpecializationView(generics.RetrieveAPIView):
    queryset = Specialization.objects.all()
    serializer_class = DoctorsOfSpecializationSerializer
    lookup_field = "pk"
    lookup_url_kwarg = "specialization_id"
