from django.contrib import admin
from .models import CompanyProfile, ReferClient


# Register your models here.


class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['company', 'company_location', 'company_date_created']
    # list_filter = 'company_location',
    search_fields = ['company', 'company_location']


admin.site.register(CompanyProfile, CompanyProfileAdmin)


class ReferClientAdmin(admin.ModelAdmin):
    list_display = ['referrer', 'client_name', 'location', 'contact_person_name', 'contact_number', 'created_date']
    search_fields = ['referrer', 'client_name', 'location']


admin.site.register(ReferClient, ReferClientAdmin)