from django.contrib import admin

# Register your models here.

from .models import *



class ApplicantAdmin(admin.ModelAdmin):
    
    list_display=('firstname', 'lastname', 'email', 'phone', 'address', 'amount', 'course', 'center', 'mode')
    
    list_filter=('firstname', 'lastname', 'email', 'address', 'course', 'center', 'date')
 
    
admin.site.register(Applicants, ApplicantAdmin)

