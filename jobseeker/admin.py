from django.contrib import admin
from jobseeker.models import Jobseeker, ReferCandidate


# Register your models here.


class JobseekerAdmin(admin.ModelAdmin):
    list_display = ['name', 'current_company_name', 'current_designation', 'present_location', 'experience',
                    'notice_period', 'feedback_update']
    list_filter = ('present_location', 'industry')
    search_fields = ['contact_number', 'current_designation', 'present_location']


admin.site.register(Jobseeker, JobseekerAdmin)


class ReferCandidateAdmin(admin.ModelAdmin):
    list_display = ['candidate_referrer', 'refer_for_the_post_of', 'candidate_name', 'current_designation',
                    'contact_number', 'present_location']


admin.site.register(ReferCandidate, ReferCandidateAdmin)
