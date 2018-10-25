from django.conf.urls import url, include
from .views import CompanyProfileDetailView, client_refer

urlpatterns = [
    url(r'^client-refer/$', client_refer, name='client-refer'),
    url(r'^(?P<slug>[-\w]+)/$', CompanyProfileDetailView.as_view(), name='company-detail'),
]