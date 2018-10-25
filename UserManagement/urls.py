from django.conf.urls import url
from .views import looking_for_job

urlpatterns = [
    url(r'^looking-for-job/$', looking_for_job, name='looking-for-job'),
]
