from jobopening.views import JobopeningListView, JobopeningDetailView, IndustryListView, \
    FunctionalAreaListView, TagIndexView, LocationListView
from django.conf.urls import url
from jobopening.views import job_submit, apply, job_search

urlpatterns = [
    url(r'^job/$', JobopeningListView.as_view(), name='jobopening-list'),
    url(r'^job-submit/$', job_submit, name='post-job'),
    url(r'^apply/$', apply, name='apply'),
    url(r'^search/$', job_search, name='search'),

    url(r'^industry/(?P<slug>[-\w]+)/$', IndustryListView.as_view(), name='industry'),
    url(r'^functional-area/(?P<slug>[-\w]+)/$', FunctionalAreaListView.as_view(), name='functional_area'),
    url(r'^location/(?P<slug>[-\w]+)/$', LocationListView.as_view(), name='location'),
    url(r'^job/(?P<slug>[-\w]+)/$', JobopeningDetailView.as_view(), name='job-detail'),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagIndexView.as_view(), name='tagged'),

]
