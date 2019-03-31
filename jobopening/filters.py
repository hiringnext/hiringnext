from .models import Jobopening, Industry
import django_filters


class JobFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(lookup_expr='icontains', label='By Job Title')

    class Meta:
        model = Jobopening
        fields = ['job_title', 'job_location', 'industry']


class IndustryJobFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(lookup_expr='icontains', label='By Job Title')

    class Meta:
        model = Industry
        fields = ['job_title', 'industry']
