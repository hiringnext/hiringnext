from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

# Create your views here.


@login_required()
def dashboard_jobseeker_index_view(request):
    return render(request, 'dashboard/dashboard-jobseeker.html', {})


@login_required()
def dashboard_referer_index_view(request):
    return render(request, 'dashboard/dashboard-referer.html', {})

