from rest_framework import serializers
from doctors.models import Department, Doctor, DoctorAvailability, MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_email(self, value):
        if "@example.com" in value:
            return value
        raise serializers.ValidationError("The domain of the email should be @example.com")

    def validate(self, attrs):
        if len(attrs['contact_number']) < 10 and attrs["is_on_vacation"]:
            raise serializers.ValidationError("Please, you should let a valid number before vacation")
        return super().validate(attrs)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'