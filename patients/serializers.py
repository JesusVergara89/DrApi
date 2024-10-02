from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord

class PatientSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
    class Meta:
        model = Patient
        fields = [
            "id",
            "first_name",
            "date_of_bith",
            "contact_number",
            "email",
            "address",
            "medical_history",
            "appointments"
        ]

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'