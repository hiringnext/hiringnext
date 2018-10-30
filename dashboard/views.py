from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from employer.models import CompanyProfile
from jobopening.models import Jobopening

# Create your views here.
from jobseeker.models import Jobseeker


@login_required()
def admin_dashboard(request):
    context = {
        'admin_dash': Jobopening.objects.all(),
        'total_opening': Jobopening.objects.all(),
        'total_companies': CompanyProfile.objects.all(),
        'total_profiles': Jobseeker.objects.all(),
        'total_revenues': '11111111',
        'monthly_revenues': '11111',
        'total_closed_positions': '1111',

    }
    return render(request, 'dashboard_admin/index.html', context)


@login_required()
def total_job_opening_list(request):
    context = {
        'job_opening_list': Jobopening.objects.all(),
    }
    return render(request, 'dashboard_admin/table-data.html', context)
