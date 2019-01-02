from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.admin.views.decorators import staff_member_required
from employer.models import CompanyProfile
from jobopening.models import Jobopening

# Create your views here.
from jobseeker.models import Jobseeker, ReferCandidate


# def admin_dashboard(request):
#     total_jobseekers = Jobseeker.objects.count(),
#     total_job_reffer = ReferCandidate.objects.count(),
#     all_seekers_profiles = total_jobseekers + total_job_reffer
#     context = {
#         'admin_dash': Jobopening.objects.all(),
#         'total_opening': Jobopening.objects.all(),
#         'total_companies': CompanyProfile.objects.all(),
#         'total_profiles': Jobseeker.objects.all(),
#         'total_revenues': '11111111',
#         'monthly_revenues': '11111',
#         'total_closed_positions': '1111',
#         'all_finders' : all_seekers_profiles,
#         'assign_recruiter': Jobopening.objects.all(),
#
#     }
#
#     return render(request, 'new_theme/dashboard/dashboard.html', context)


class AdminDashboard(ListView):
    model = Jobseeker
    template_name = 'new_theme/dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(AdminDashboard, self).get_context_data(**kwargs)
        context.update({
            'admin_dash': Jobopening.objects.all(),
            'total_opening': Jobopening.objects.all(),
            'total_companies': CompanyProfile.objects.all(),
            'total_profiles': Jobseeker.objects.all(),
            'total_revenues': '11111111',
            'monthly_revenues': '11111',
            'total_closed_positions': '1111',
            'all_finders': Jobseeker.objects.count() + ReferCandidate.objects.count(),
            'total_job_referrer': ReferCandidate.objects.all(),
            'assign_recruiter': Jobopening.objects.all(),
            'job_opening_list': Jobopening.objects.all(),

        })

        return context


@login_required()
def total_job_opening_list(request):
    context = {
        'job_opening_list': Jobopening.objects.all(),
    }
    return render(request, 'dashboard_admin/active_openings.html', context)


@login_required()
def total_resume_list(request):
    context = {
        'job_resume_list': Jobseeker.objects.all(),
    }
    return render(request, 'dashboard_admin/active_resumes.html', context)
