from .models import Shop
from rest_framework import serializers


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields='__all__'
        # fields= ['id', 'fullname','email', 'subject', 'phone', 'message']