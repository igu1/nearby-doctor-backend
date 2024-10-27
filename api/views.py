from rest_framework import generics
from .models import Doctor, Specialization
from .serializers import (
    DoctorSerializer,
    SpecializationSerializer,
    DoctorsOfSpecializationSerializer,
)


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
    lookup_field = 'pk'
    lookup_url_kwarg = 'specialization_id'
