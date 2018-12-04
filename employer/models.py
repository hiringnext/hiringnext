from django.utils import timezone
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from ecommerce.choice.job_location import JOB_LOCATION_CHOICES

AUTH_USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


# Create your models here.


class CompanyProfile(models.Model):
    company = models.CharField(max_length=50)
    slug = models.SlugField(max_length=40)
    company_profile = models.TextField()
    company_location = models.CharField(choices=JOB_LOCATION_CHOICES, max_length=50)
    company_website = models.URLField(verbose_name='Website', default=None)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    total_employees = models.PositiveIntegerField(null=True, blank=True)
    company_review = models.DecimalField(decimal_places=1, max_digits=2, null=True, blank=True, help_text="Rate Company Out Of Five")
    company_date_created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.company

    def save(self, *args, **kwargs):
        self.slug_field = slugify(self.company)
        super(CompanyProfile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'slug': self.slug})


class ReferClient(models.Model):
    referrer = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="referred_by",
        null=True,
        blank=True
    )
    client_name = models.CharField(max_length=70)
    location = models.CharField(choices=JOB_LOCATION_CHOICES, max_length=50)
    contact_person_name = models.CharField(max_length=50, verbose_name='Contact Name')
    contact_number = models.PositiveIntegerField()
    contact_email_id = models.EmailField(max_length=50)

    position_required = models.CharField(max_length=500)
    no_of_requirement = models.PositiveIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_created=True, null=True)
