from .models import Contacts
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contacts
        fields='__all__'
        # fields= ['id', 'fullname','email', 'subject', 'phone', 'message']