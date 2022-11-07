from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.

class Shop(models.Model):
    image=models.ImageField(upload_to='img')
    name=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=200, null=True)
    price=models.CharField(max_length=200, null=True)
    date=models.DateTimeField(auto_now_add=True)
