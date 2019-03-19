from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.db.models import Q
from django.urls import reverse

from ecommerce.choice.experience import EXPERIENCE_CHOICE
from ecommerce.choice.job_location import JOB_LOCATION_CHOICES
from ecommerce.choice.qualification import QUALIFICATION_CHOICES
from ecommerce.choice.bond_security_issue import BOND_OR_SECURITY
from ecommerce.choice.employment_type import EMPLOYMENT_TYPE

from django.template.defaultfilters import slugify
from employer.models import CompanyProfile
from taggit.managers import TaggableManager

# Create your models here.


class JobOpeningQueryset(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class JobOpeningManager(models.Manager):
    def get_queryset(self):
        return JobOpeningQueryset(self.model, using=self._db)

    def all(self, **kwargs):
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


class DefaultIndustry(models.Model):
    defindustry = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.defindustry

    def save(self, *args, **kwargs):
        self.slug_field = slugify(self.defindustry)
        super(DefaultIndustry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("default-industry", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["id"]


class Industry(models.Model):
    industry = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.industry

    def save(self, *args, **kwargs):
        self.slug_field = slugify(self.industry)
        super(Industry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("industry", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["id"]


class FunctionalArea(models.Model):
    industry = models.ForeignKey(Industry)
    default_industry = models.ForeignKey('Industry', related_name='Default_Industry', null=True, blank=True)
    functional_area = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.functional_area

    def save(self, *args, **kwargs):
        self.slug_field = slugify(self.functional_area)
        super(FunctionalArea, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("functional_area", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["id"]


class JobLocation(models.Model):
    job_location = models.CharField(choices=JOB_LOCATION_CHOICES, null=True, blank=True, max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.job_location

    def save(self, *args, **kwargs):
        self.slug_field = slugify(self.job_location)
        super(JobLocation, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('location', kwargs={'slug': self.slug})

    class Meta:
        ordering = ["id"]


class ApplicationQuestions(models.Model):
    questions_for = models.CharField(max_length=50)

    def __str__(self):
        return self.questions_for


class Jobopening(models.Model):
    assign_recruiter = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Recruiter_Handling",
        null=True,
        blank=True,
    )
    job_title = models.CharField(max_length=50, verbose_name='Designation', editable=True)
    slug = models.SlugField(max_length=40)
    company_name = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, verbose_name='Company Name')
    job_location = models.ForeignKey(JobLocation, on_delete=models.CASCADE, verbose_name='Job Location')
    job_location_sample = models.CharField(choices=JOB_LOCATION_CHOICES, max_length=20, null=True,
                                           verbose_name='Sample Job Location')
    experience = models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Experience')
    experience_choice = models.DecimalField(choices=EXPERIENCE_CHOICE, decimal_places=0, max_digits=3, null=True, blank=True)
    skill = models.CharField(max_length=100, verbose_name='Skills')
    qualification = models.CharField(choices=QUALIFICATION_CHOICES, max_length=100, verbose_name='Qualification')
    min_salary_budget = models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Min. Salary Criteria', help_text='Mention Salary in Annual Packages only')
    max_salary_budget = models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Max. Salary Criteria', help_text='Mention Salary in Annual Packages only')
    referral_reward = models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='Referral Amount')
    industry = models.ForeignKey(Industry, null=True, blank=True)
    functional_area = models.ForeignKey(FunctionalArea, null=True, blank=True)
    default_industry = models.ForeignKey(DefaultIndustry, null=True, blank=True)
    role_category = models.CharField(max_length=50, verbose_name='Role Category')
    employment_type = models.CharField(choices=EMPLOYMENT_TYPE, max_length=100, verbose_name='Employment Type')
    job_description = models.TextField(verbose_name='Job Summary', null=True, blank=True)
    job_objective = models.TextField(verbose_name='Job Objectives', null=True, blank=True)
    must_have_skills = models.TextField(verbose_name='Must Have Skills', null=True, blank=True)
    bond_or_security = models.CharField(choices=BOND_OR_SECURITY, null=True, max_length=20, blank=True,
                                           verbose_name='Bond Or Security')

    nice_to_have = models.CharField(max_length=500, verbose_name='Nice To Have', null=True)
    job_created = models.DateTimeField(auto_created=True, null=True)
    active = models.BooleanField(default=True)
    Questions = models.ManyToManyField(ApplicationQuestions, default=None, verbose_name='Application Questionnaires')

    objects = JobOpeningManager()
    tags = TaggableManager()

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

    def get_tag_url(self):
        return reverse("tagged", kwargs={"slug": self.slug})



