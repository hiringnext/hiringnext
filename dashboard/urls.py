from django.conf import settings
from django.conf.urls import url

from .views import admin_dashboard, total_job_opening_list

urlpatterns = [
    url(r'^e-dashboard/$', admin_dashboard, name='dashboard-admin'),
    url(r'^active-openings/$', total_job_opening_list, name='active_openings'),

]
