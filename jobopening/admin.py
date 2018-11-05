from django.contrib import admin
from .models import Jobopening, ApplicationQuestions, JobLocation, JobApply


# Register your models here.


class JobopeningAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'company_name', 'job_location', 'salary_budget', 'referral_reward', 'job_created']
    list_filter = ('job_location', 'industry')
    search_fields = ['job_title', 'job_location', 'industry']


admin.site.register(Jobopening, JobopeningAdmin)
admin.site.register(ApplicationQuestions)
admin.site.register(JobLocation)
admin.site.register(JobApply)

