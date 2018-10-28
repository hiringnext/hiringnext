from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from employer.models import CompanyProfile
from jobseeker.forms import ReferCandidateForm
from .forms import JobopeningForm, ApplyForm
from .models import Jobopening, ApplicationQuestions, JobLocation
from django.views.generic.edit import FormMixin


class JobopeningListView(FormMixin, ListView):
    model = Jobopening
    form_class = ReferCandidateForm
    context_object_name = 'opening'
    template_name = "job_list.html"
    ordering = ['-job_created']

    def get_success_url(self):
        return HttpResponseRedirect('/job/')

    def get_context_data(self, **kwargs):
        context = super(JobopeningListView, self).get_context_data(**kwargs)
        context['location'] = JobLocation.objects.all(),
        context['questions'] = Jobopening.objects.all(),
        context['form'] = self.get_form()
        context['query'] = self.request.GET.get('q')
        return context

    def POST(self, request, form):
        form = form(request.POST or None)
        context = {
            "form": form,
        }

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/job/')

            # if a GET (or any other method) we'll create a blank form
        return render(request, 'job_list.html', context)

    def get_queryset(self):
        queryset_list = Jobopening.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(job_title__icontains=query) |
                Q(job_location__slug__icontains=query) |
                Q(industry__icontains=query) |
                Q(functional_area__icontains=query)
            ).distinct()

        return queryset_list


class JobApplyListView(DetailView):
    model = ApplicationQuestions
    template_name = 'apply_form.html'

    def get_context_data(self, **kwargs):
        context = super(JobApplyListView, self).get_context_data(**kwargs)
        return context


class JobopeningDetailView(DetailView):
    model = Jobopening
    template_name = "job_details.html"

    def get_context_data(self, **kwargs):
        context = super(JobopeningDetailView, self).get_context_data(**kwargs)
        context['company'] = CompanyProfile.objects.all(),
        return context


@login_required()
def job_submit(request):
    job_opening_form = JobopeningForm(request.POST or None)
    context = {
        "form": job_opening_form,
    }
    # if this is a POST request we need to process the form data
    if job_opening_form.is_valid():
        job_opening_form.save()
        return HttpResponseRedirect('/job/')

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'job_post_2.html', context)


@login_required()
def apply(request):
    job_apply_form = ApplyForm(request.POST or None)
    context = {
        "form": ApplyForm,
    }
    # if this is a POST request we need to process the form data
    if job_apply_form.is_valid():
        job_apply_form.save()
        return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    return render(request, 'apply_form.html', context)


class LocationListView(ListView):
    model = JobLocation
    template_name = 'job_list.html'
    context_object_name = 'by_location_openings'

    def get_context_data(self, **kwargs):
        context = super(LocationListView, self).get_context_data(**kwargs)
        return context
