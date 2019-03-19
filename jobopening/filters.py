from .models import Jobopening
import django_filters


class JobFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(lookup_expr='icontains',)

    class Meta:
        model = Jobopening
        fields = ['job_location','industry' ]
