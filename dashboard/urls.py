from django.conf import settings
from django.conf.urls import url

from .views import dashboard_jobseeker_index_view, dashboard_referer_index_view

urlpatterns = [
    url(r'^jobseeker/$', dashboard_jobseeker_index_view, name='dashboard-jobseeker-index'),
    url(r'^referer/$', dashboard_referer_index_view, name='dashboard-referer-index'),

]
