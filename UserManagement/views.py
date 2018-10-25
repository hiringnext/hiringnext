from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import LookingForJob
from .form import LookingForJobForm


def looking_for_job(request):
    looking_for_job_form = LookingForJobForm(request.POST or None)
    context = {
        "form": looking_for_job_form,
    }
    # if this is a POST request we need to process the form data
    if looking_for_job_form.is_valid():
        looking_for_job_form.save()
        return HttpResponseRedirect('/job/')

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'signup_forms/looking_for_job.html', context)
