from rest_framework import serializers

from MedicalApp.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["name", "license_no", "address", "contact_no", "email", "description"]

