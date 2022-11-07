from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ShopSerializer
from .models import Shop


# Create your views here.

class ShopViewSet(viewsets.ModelViewSet):
    queryset=Shop.objects.all().order_by('-id')
    serializer_class=ShopSerializer

