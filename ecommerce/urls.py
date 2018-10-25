"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from jobseeker.views import IndexListView
from .views import home_page, about_page, contact_page


urlpatterns = [
    url(r'^$', IndexListView.as_view(), name='index'),
    url(r'^home/$', home_page),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),

    # Employer URL
    url(r'^company/', include('employer.urls')),
    # Job Opening URL
    url(r'^', include('jobopening.urls')),
    # Job Seeker URL
    url(r'^', include('jobseeker.urls')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^admin/', admin.site.urls),
    # other urls
    url(r"^referrals/", include("pinax.referrals.urls", namespace="pinax_referrals")),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
