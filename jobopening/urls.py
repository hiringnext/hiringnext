from jobopening.views import JobopeningListView, JobopeningDetailView, LocationListView
from django.conf.urls import url
from jobopening.views import job_submit, apply


urlpatterns = [
    url(r'^job/$', JobopeningListView.as_view(), name='jobopening-list'),
    url(r'^job-submit/$', job_submit, name='post-job'),
    url(r'^apply/$', apply, name='apply'),
    url(r'^location/(?P<slug>[-\w]+)/$', LocationListView.as_view(), name='location'),
    url(r'^job/(?P<slug>[-\w]+)/$', JobopeningDetailView.as_view(), name='job-detail'),

]