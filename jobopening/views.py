from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView

from employer.models import CompanyProfile
from jobseeker.forms import ReferCandidateForm
from .forms import JobopeningForm, ApplyForm
from .models import Jobopening, ApplicationQuestions, JobLocation, Industry, FunctionalArea
from django.views.generic.edit import FormMixin
from taggit.models import Tag


class TagMixin(object):
    def get_context_data(self, kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class JobopeningListView(TagMixin, FormMixin, ListView):
    model = Jobopening
    form_class = ReferCandidateForm
    context_object_name = 'opening'
    template_name = "job_list.html"
    ordering = ['-job_created']

    def get_context_data(self, **kwargs):
        context = super(JobopeningListView, self).get_context_data(kwargs)
        context.update({
            'industry': Industry.objects.all(),
            'function_area': FunctionalArea.objects.all(),
            'location': JobLocation.objects.all(),
            'questions': ApplicationQuestions.objects.all(),
            'form': self.get_form(),
            'query': self.request.GET.get('q')
        })
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

    def get_success_url(self):
        return HttpResponseRedirect('/job/')

    def get_queryset(self):
        queryset_list = Jobopening.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(job_title__icontains=query) |
                Q(job_location__slug__icontains=query)
            ).distinct()

        return queryset_list


class IndustryListView(DetailView):
    model = Industry
    queryset = Industry.objects.all()
    template_name = 'industry/industry_list.html'

    def get_context_data(self, **kwargs):
        context = super(IndustryListView, self).get_context_data(**kwargs)
        context.update({
            'main_industry': Industry.objects.all(),
            'jobopening': Jobopening.objects.all(),
            'function_area': FunctionalArea.objects.all(),
            # 'location': JobLocation.objects.all(),
            'questions': ApplicationQuestions.objects.all(),
             })
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


class FunctionalAreaListView(DetailView):
    model = FunctionalArea
    queryset = FunctionalArea.objects.all()
    form_class = ReferCandidateForm
    template_name = 'functional_area/functional_area.html'

    def get_context_data(self, **kwargs):
        context = super(FunctionalAreaListView, self).get_context_data(**kwargs)
        context.update({
            'opening': Jobopening.objects.all(),
            'industry': Industry.objects.all(),

        })
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

    def get_success_url(self):
        return HttpResponseRedirect('/job/')


class JobopeningDetailView(TagMixin, DetailView):
    model = Jobopening
    template_name = "job_details.html"

    def get_context_data(self, **kwargs):
        context = super(JobopeningDetailView, self).get_context_data(kwargs)
        context.update({
            'company': CompanyProfile.objects.all(),
            'industry': Industry.objects.all(),
            'function_area': FunctionalArea.objects.all(),
        })
        return context


class TagIndexView(TagMixin, ListView):
    model = Jobopening
    queryset = Jobopening.objects.all()
    template_name = 'tag/tag_detail.html'

    def get_queryset(self):
        return Jobopening.objects.filter(tags__slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super(TagIndexView, self).get_context_data(kwargs)
        context.update({
            'industry': Industry.objects.all(),
            'function_area': FunctionalArea.objects.all(),
            # 'location': JobLocation.objects.all(),
            'questions': ApplicationQuestions.objects.all(),

        })
        return context


class LocationListView(FormMixin, ListView):
    model = JobLocation
    form_class = ReferCandidateForm
    template_name = 'industry/industry_detail.html'
    context_object_name = 'by_location_openings'

    def get_context_data(self, **kwargs):
        context = super(LocationListView, self).get_context_data(**kwargs)
        context.update({
            'industry': Industry.objects.all(),
            'function_area': FunctionalArea.objects.all(),
            # 'location': JobLocation.objects.all(),
            'questions': ApplicationQuestions.objects.all(),
            'form': self.get_form(),
            'query': self.request.GET.get('q')
        })
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

    def get_success_url(self):
        return HttpResponseRedirect('/job/')

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


class JobApplyListView(DetailView):
    model = ApplicationQuestions
    template_name = 'apply_form.html'

    def get_context_data(self, **kwargs):
        context = super(JobApplyListView, self).get_context_data(**kwargs)
        return context
