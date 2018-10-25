from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from employer.models import CompanyProfile
from .forms import JobopeningForm, ApplyForm
from .models import Jobopening, ApplicationQuestions, JobLocation


class JobopeningListView(ListView):
    model = Jobopening
    template_name = "job_list.html"
    ordering = ['-job_created']

    def get_context_data(self, **kwargs):
        context = super(JobopeningListView, self).get_context_data(**kwargs)
        context['questions'] = Jobopening.objects.all(),
        context['location'] = JobLocation.objects.all(),
        context['query'] = self.request.GET.get('q')
        return context

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

    # def get_queryset(self):
    #     request = self.request
    #     query = request.GET.get('q', None)
    #
    #     if query is not None:
    #         job_opening_result = Jobopening.objects.search(query)
    #
    #
    #         # combine querysets
    #         queryset_chain = chain(
    #             job_opening_result
    #
    #         )
    #         qs = sorted(queryset_chain,
    #                     key=lambda instance: instance.pk,
    #                     reverse=True)
    #         return qs
    #     return Jobopening.objects.none()  # just an empty queryset as default

    # def advanced_search(self, form):
    #     # It's easier to store a dict of the possible lookups we want, where
    #     # the values are the keyword arguments for the actual query.
    #     qdict = {'job_location': 'job_location__slug__icontains',
    #              'job_title': 'job_title__icontains',
    #              'company_name': 'company_name__company__icontains',
    #
    #              }
    #
    #     # Then we can do this all in one step instead of needing to call
    #     # 'filter' and deal with intermediate data structures.
    #     q_objs = [Q(**{qdict[k]: form.cleaned_data[k]}) for k in qdict.keys() if form.cleaned_data.get(k, None)]
    #     search_results = Jobopening.objects.select_related().filter(*q_objs)
    #     return search_results


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


# def job_list(request):
#     return render(request, "job_list.html", {})


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
