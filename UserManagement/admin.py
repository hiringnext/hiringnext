from django.contrib import admin
from .models import LookingForJob


# Register your models here.

class LookingforJobAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email']
    search_fields = ['phone_number', 'email', 'first_name']


admin.site.register(LookingForJob, LookingforJobAdmin)
