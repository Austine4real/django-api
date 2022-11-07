from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contacts


# Create your views here.

class ContactsViewSet(viewsets.ModelViewSet):
    queryset=Contacts.objects.all().order_by('-id')
    serializer_class=ContactSerializer

