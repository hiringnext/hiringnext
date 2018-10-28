from django.db import models
from django.db.models import Q
from django.urls import reverse

from ecommerce.choice.job_location import JOB_LOCATION_CHOICES
from ecommerce.choice.qualification import QUALIFICATION_CHOICES
from ecommerce.choice.functional_area import FUNCTIONAL_AREA_CHOICES
from django.template.defaultfilters import slugify
from employer.models import CompanyProfile


# Create your models here.


class JobOpeningQueryset(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class ApplicationQuestions(models.Model):
    questions_for = models.CharField(max_length=50)

    def __str__(self):
        return self.questions_for


##############################################################
# Sample for Location Manager


class LocationQuerySet(models.QuerySet):
    def Vadodara(self):
        return self.filter(job_location_sample='Vad')

    def Ahmedabad(self):
        return self.filter(job_location_sample='Ahm')

    def Surat(self):
        return self.filter(job_location_sample='Sur')

    def Rajkot(self):
        return self.filter(job_location_sample='Raj')


class LocationManager(models.Manager):
    def get_queryset(self):
        return LocationQuerySet(self.model, using=self._db)

    def Vadodara(self):
        return self.get_queryset().Vadodara()

    def Ahmedabad(self):
        return self.get_queryset().Ahmedabad()

    def Surat(self):
        return self.get_queryset().Surat()

    def Rajkot(self):
        return self.get_queryset().Rajkot()


##########################


class JobLocation(models.Model):
    job_location = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)

    def __str__(self):
        return self.job_location

    def save(self, *args, **kwargs):
        self.slug_field = slugify(self.job_location)
        super(JobLocation, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('location', kwargs={'slug': self.slug})


class JobOpeningManager(models.Manager):
    def get_queryset(self):
        return JobOpeningQueryset(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()

    def get_related(self, instance):
        jobopening_one = self.get_queryset().filter(industry__in=instance.industry.all())
        jobopening_two = self.get_queryset().filter(default=instance.default)
        qs = (jobopening_one | jobopening_two).exclude(id=instance.id).distinct()
        return qs

    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(job_title__icontains=query) |
                         Q(job_location__slug__icontains=query) |
                         Q(industry__icontains=query) |
                         Q(functional_area__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class Jobopening(models.Model):
    job_title = models.CharField(max_length=50, verbose_name='Designation')
    slug = models.SlugField(max_length=40)
    company_name = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, verbose_name='Company Name')
    job_location = models.ForeignKey(JobLocation, on_delete=models.CASCADE, verbose_name='Job Location')
    job_location_sample = models.CharField(choices=JOB_LOCATION_CHOICES, max_length=20, null=True,
                                           verbose_name='Sample Job Location')
    experience = models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Experience')
    skill = models.CharField(max_length=100, verbose_name='Skills')
    # qualification = models.CharField(max_length=50)
    qualification = models.CharField(choices=QUALIFICATION_CHOICES, max_length=100, verbose_name='Qualification')
    salary_budget = models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='Salary Criteria')
    # company_profile = models.TextField()
    referral_reward = models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='Referral Amount')
    industry = models.CharField(max_length=50, verbose_name='Industry')
    functional_area = models.CharField(choices=FUNCTIONAL_AREA_CHOICES, max_length=100, verbose_name='Functional Area')
    role_category = models.CharField(max_length=50, verbose_name='Role Category')
    employment_type = models.CharField(max_length=50, verbose_name='Employment Type')
    job_description = models.TextField(verbose_name='Job Description')
    nice_to_have = models.CharField(max_length=500, verbose_name='Nice To Have', null=True)
    job_created = models.DateTimeField(auto_created=True, null=True)
    active = models.BooleanField(default=True)
    Questions = models.ManyToManyField(ApplicationQuestions, default=None, verbose_name='Application Questionnaires')

    objects = JobOpeningManager()
    job_location_manager = LocationManager()

    def __str__(self):
        return self.job_title

    class Meta:
        ordering = ["-job_created"]

    def save(self, *args, **kwargs):
        if not self.slug and self.job_title:
            self.slug = slugify(self.job_title)
        super(Jobopening, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'slug': self.slug})


class JobApply(models.Model):
    title = models.ForeignKey(Jobopening, max_length=100, default=True)
    apply_for = models.CharField(max_length=50, default=True)
    question_one = models.CharField(max_length=100, default=True)
    question_two = models.CharField(max_length=100, default=True)
    question_three = models.CharField(max_length=100, default=True)
    question_four = models.CharField(max_length=100, default=True)
    question_five = models.CharField(max_length=100, default=True)

    def __str__(self):
        return self.apply_for
