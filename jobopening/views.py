from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView

from ecommerce.choice.job_location import JOB_LOCATION_CHOICES
from ecommerce.forms import ContactForm
from employer.models import CompanyProfile
from jobseeker.forms import ReferCandidateForm
from jobseeker.models import Jobseeker
from .forms import JobopeningForm, JobApplyForm
from .models import Jobopening, ApplicationQuestions, JobLocation, Industry, FunctionalArea
from django.views.generic.edit import FormMixin, FormView
from taggit.models import Tag
from django.shortcuts import render
from .filters import JobFilter


class TagMixin(object):
    def get_context_data(self, kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.distinct()
        return context

# Home Page

class IndexListView(TagMixin, ListView):
    model = Jobopening
    template_name = 'new_theme/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(kwargs)
        context.update({
            'total_opening': Jobopening.objects.all(),
            'total_companies' : CompanyProfile.objects.all(),
            'total_profiles' : Jobseeker.objects.all(),
            'industry': Industry.objects.filter(jobopening__functional_area__industry__isnull=False).distinct(),
            'function_area': FunctionalArea.objects.all(),
            'location': JobLocation.objects.all(),
            'questions': ApplicationQuestions.objects.all(),
            'location_choice': JOB_LOCATION_CHOICES,
            'new_jobs': Jobopening.objects.all().order_by('-job_created').distinct()[:6],
            'query': self.request.GET.get('q')
        })

        return context

    def get_queryset(self):
        queryset_list = Jobopening.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(job_title__icontains=query) |
                Q(company_name__company__icontains=query)
            ).distinct()
        return queryset_list


class JobopeningListView(TagMixin, FormMixin, ListView):
    model = Jobopening
    form_class = ReferCandidateForm
    context_object_name = 'opening'
    template_name = "new_theme/jobs-list-layout-2.html"
    paginate_by = 5
    ordering = ['-job_created']

    def get_context_data(self, **kwargs):
        context = super(JobopeningListView, self).get_context_data(kwargs)
        context.update({
            'industry': Industry.objects.all(),
            'function_area': FunctionalArea.objects.all(),
            'location': JobLocation.objects.all(),
            'questions': ApplicationQuestions.objects.all(),
            'location_choice': JOB_LOCATION_CHOICES,
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
        return render(request, 'new_theme/jobs-list-layout-2.html', context)

    def get_success_url(self):
        return HttpResponseRedirect('/job/')

    def get_queryset(self):
        queryset_list = Jobopening.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(job_title__icontains=query)
            )

        return queryset_list

    def job_search_filter(request):
        job_list = Jobopening.objects.all()
        job_filter = JobFilter(request.GET, queryset=job_list)
        return render(request, 'new_theme/jobs-list-layout-2.html', {'filter': job_filter})


def job_search_filter(request):
    job_list = Jobopening.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'new_theme/jobs-list-layout-2.html', {'filter': job_filter})


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
            'industry': Industry.objects.all(),
            'location': JobLocation.objects.all(),
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


class FunctionalAreaListView(DetailView):
    model = Industry
    queryset = FunctionalArea.objects.all()
    form_class = ReferCandidateForm
    template_name = 'functional_area/jobs-list-functional-area.html'

    def get_context_data(self, **kwargs):
        context = super(FunctionalAreaListView, self).get_context_data(**kwargs)
        context.update({
            'opening': Jobopening.objects.all(),
            'industry': Industry.objects.all(),
            'function_area': FunctionalArea.objects.all(),
            'location': JobLocation.objects.all(),
            'questions': ApplicationQuestions.objects.all(),
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


class JobopeningDetailView(TagMixin, FormMixin, DetailView):
    model = Jobopening
    form_class = JobApplyForm
    template_name = "new_theme/single-job-page.html"

    def get_context_data(self, **kwargs):
        context = super(JobopeningDetailView, self).get_context_data(kwargs)
        context.update({
            'company': CompanyProfile.objects.all(),
            'industry': Industry.objects.all(),
            'function_area': FunctionalArea.objects.all().annotate(),
            'question_list': ApplicationQuestions.objects.all(),
            'similar_job': FunctionalArea.objects.all().distinct()[:5].annotate(),

        })
        return context

    def form_valid(self, form):
        form.save(commit=True)
        return super(JobopeningDetailView, self).form_valid(form)


    # def apply(self, request):
    #     form = JobApplyForm(request.POST or None)
    #     context = {
    #         "form": form,
    #         }
    #
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/job/')
    #
    #     return render(request, 'new_theme/single-job-page.html', context)


class ApplyFormView(FormView):
    template_name = 'new_theme/single-job-page.html'
    form_class = JobApplyForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.save(commit=True)
        return super(ApplyFormView, self).form_valid(form)


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


class LocationListView(DetailView):
    model = JobLocation
    queryset = JobLocation.objects.all()
    template_name = 'location_wise_job_opening.html'

    def get_context_data(self, **kwargs):
        context = super(LocationListView, self).get_context_data(**kwargs)
        context.update({
            'industry': Industry.objects.all(),
            'function_area': FunctionalArea.objects.all(),
            # 'location': JobLocation.objects.all(),
            'questions': ApplicationQuestions.objects.all(),
            'opening': Jobopening.objects.all(),
            'location': JobLocation.objects.all(),
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


def job_search(request):

    if request.method == 'GET':
        search_job_by_title = request.GET.get('q')
        try:
            status = Jobopening.objects.filter(job_title__icontains=search_job_by_title)
        except Jobopening.DoesNotExist:
            status = None

        context = {
            'jobs': status,
            'industry': Industry.objects.all(),
            'function_area': FunctionalArea.objects.all(),
            'location': JobLocation.objects.all(),
            'questions': ApplicationQuestions.objects.all(),
        }
        return render(request, "search_bar.html", context)

    else:
        return request(request, "search_bar.html", {})


def contact_us(request):
    contact_us_form = ContactForm(request.POST or None)
    context = {
        "form": contact_us_form,
    }
    # if this is a POST request we need to process the form data
    if contact_us_form.is_valid():
        contact_us_form.save(request)
        return HttpResponseRedirect('/job/')

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'new_theme/pages-contact.html', context)
