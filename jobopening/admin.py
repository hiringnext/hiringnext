from django.contrib import admin
from .models import Jobopening, ApplicationQuestions, JobLocation, Industry, FunctionalArea, DefaultIndustry


# Register your models here.


class JobopeningAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'company_name', 'job_location', 'min_salary_budget','max_salary_budget','referral_reward', 'job_created', 'tag_list']
    list_filter = ('job_location', 'industry')
    search_fields = ['job_title', 'job_location', 'industry']

    def get_queryset(self, request):
        return super(JobopeningAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())



admin.site.register(Jobopening, JobopeningAdmin)
admin.site.register(Industry)
admin.site.register(FunctionalArea)
admin.site.register(ApplicationQuestions)
admin.site.register(JobLocation)
admin.site.register(DefaultIndustry)


