from django.urls import path
from .views import (
    DoctorListCreateView,
    DoctorRetrieveUpdateDestroyView,
    SpecializationListCreateView,
    SpecializationRetrieveUpdateDestroyView,
    DoctorListBySpecializationView,
)

urlpatterns = [
    path("doctors/", DoctorListCreateView.as_view(), name="doctor-list-create"),
    path(
        "doctors/<int:pk>/",
        DoctorRetrieveUpdateDestroyView.as_view(),
        name="doctor-retrieve-update-destroy",
    ),
    path(
        "specializations/",
        SpecializationListCreateView.as_view(),
        name="specialization-list-create",
    ),
    path(
        "specializations/<int:pk>/",
        SpecializationRetrieveUpdateDestroyView.as_view(),
        name="specialization-retrieve-update-destroy",
    ),
    path(
        "specializations/<int:specialization_id>/doctors/",
        DoctorListBySpecializationView.as_view(),
        name="doctor-list-by-specialization",
    ),
]
