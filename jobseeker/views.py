from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView

from employer.models import CompanyProfile
from jobopening.models import Jobopening
from .forms import ResumeSubmitForm, ReferCandidateForm
from .models import Jobseeker, ReferCandidate


class ResumeListView(ListView):
    model = Jobseeker
    template_name = 'job_opening_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = Jobseeker.objects.all()
        return context


def resume_submit(request):
    resume_submit_form = ResumeSubmitForm(request.POST or None)
    context = {
        "form": resume_submit_form,
    }
    # if this is a POST request we need to process the form data
    if resume_submit_form.is_valid():
        resume_submit_form.save()
        return HttpResponseRedirect('/job/')

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'resume_post.html', context)


class IndexListView(ListView):
    model = Jobopening
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['total_opening'] = Jobopening.objects.all()
        context['total_companies'] = CompanyProfile.objects.all()
        context['total_profiles'] = Jobseeker.objects.all()
        return context

    def get_queryset(self):
        queryset_list = Jobopening.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(job_location__slug__icontains=query) |
                Q(job_title__icontains=query) |
                Q(company_name__company__icontains=query) |
                Q(employment_type__icontains=query)
            ).distinct()
        return queryset_list


@login_required()
def candidate_refer(request):
    candidate_refer_form = ReferCandidateForm(request.POST or None)
    context = {
        "form": candidate_refer_form,
    }
    # if this is a POST request we need to process the form data
    if candidate_refer_form.is_valid():
        candidate_refer_form.save()
        return HttpResponseRedirect('/job/')

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'candidate_refer_form.html', context)
