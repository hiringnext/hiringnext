from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from employer.forms import ClientReferForm
from jobopening.models import Jobopening
from .models import CompanyProfile, ReferClient


# Create your views here.


# class CompanyProfileListView(ListView):
#     model = CompanyProfile
#     template_name = "company_page.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['company_page'] = CompanyProfile.objects.all(),
#         return context


class CompanyProfileDetailView(DetailView):
    model = CompanyProfile
    template_name = "company_page.html"

    def get_context_data(self, **kwargs):
        context = super(CompanyProfileDetailView, self).get_context_data(**kwargs)
        context.update({
            'opening_count': CompanyProfile.objects.all(),
            'opening': Jobopening.objects.all()
        })
        return context


#
# @login_required()
# def job_submit(request):
#     job_opening_form = JobopeningForm(request.POST or None)
#     context = {
#         "form": job_opening_form,
#     }
#     # if this is a POST request we need to process the form data
#     if job_opening_form.is_valid():
#         return HttpResponseRedirect('/job/')
#
#     # if a GET (or any other method) we'll create a blank form
#     return render(request, 'job_post_2.html', context)

# def job_list(request):
#     return render(request, "job_list.html", {})

#
# class ClientReferList(ListView):
#     model = ReferClient
#     template_name = 'client_refer_form.html'


@login_required()
def client_refer(request):
    client_refer_form = ClientReferForm(request.POST or None)
    context = {
        "form": client_refer_form,
    }
    # if this is a POST request we need to process the form data
    if client_refer_form.is_valid():
        client_refer_form.save()
        return HttpResponseRedirect('/job/')

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'client_refer_form.html', context)
