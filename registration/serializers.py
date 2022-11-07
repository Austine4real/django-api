from dataclasses import fields
from .models import Applicants
from rest_framework import serializers


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Applicants
        # fields='__all__'
        fields= ['id', 'firstname','lastname','email', 'email', 'phone','amount', 'address', 'course', 'center', 'mode']