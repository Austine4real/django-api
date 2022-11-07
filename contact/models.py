from django.db import models

# Create your models here.

class Contacts(models.Model):
    fullname=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200, null=True)
    subject=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    message=models.TextField(max_length=200, null=True)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.fullname}'
