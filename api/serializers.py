from rest_framework import serializers
from .models import Doctor, Specialization


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(read_only=True)
    specialization_id = serializers.PrimaryKeyRelatedField(
        queryset=Specialization.objects.all(), source="specialization", write_only=True
    )

    class Meta:
        model = Doctor
        fields = "__all__"


class DoctorsOfSpecializationSerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(many=True, read_only=True)

    class Meta:
        model = Specialization
        fields = ["id", "name", "description", "doctors"]
