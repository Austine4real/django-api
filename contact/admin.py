from django.contrib import admin

# Register your models here.

from .models import *



class ContactAdmin(admin.ModelAdmin):
    
    list_display=('fullname', 'email', 'subject', 'phone', 'date', 'message')
    
    list_filter=( 'date', 'subject')
 
    
admin.site.register(Contacts, ContactAdmin)