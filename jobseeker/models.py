from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from ecommerce.choice.functional_area import FUNCTIONAL_AREA_CHOICES
from ecommerce.choice.job_location import JOB_LOCATION_CHOICES
from ecommerce.choice.qualification import QUALIFICATION_CHOICES
from ecommerce.choice.notice_period import NOTICE_PERIOD_CHOICES
from ecommerce.choice.gender import GENDER_CHOICES
from ecommerce.choice.candidate_feedback import CANDIDATE_FEEDBACK_CHOICES
from jobopening.models import Jobopening


class Jobseeker(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.IntegerField(null=False, unique=True)
    alternate_number = models.IntegerField(blank=True)
    email = models.EmailField(blank=False, unique=True)
    date_of_birth = models.DateField(max_length=8)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    current_designation = models.CharField(max_length=50)
    current_company_name = models.CharField(max_length=50)
    present_location = models.CharField(choices=JOB_LOCATION_CHOICES, max_length=50)
    preferred_location = models.CharField(choices=JOB_LOCATION_CHOICES, max_length=50)
    experience = models.DecimalField(decimal_places=1, max_digits=5, null=True)
    notice_period = models.CharField(choices=NOTICE_PERIOD_CHOICES, max_length=15)
    skill = models.CharField(max_length=100)
    qualification = models.CharField(choices=QUALIFICATION_CHOICES, max_length=100)
    present_salary = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    expected_salary = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    past_company_name = models.CharField(max_length=50)
    past_designation = models.CharField(max_length=50)
    industry = models.CharField(max_length=100)
    functional_area = models.CharField(choices=FUNCTIONAL_AREA_CHOICES, max_length=100)
    employment_type = models.CharField(max_length=50)
    profile_summary = models.TextField()
    resume_summary = models.TextField()
    resume = models.FileField(upload_to='documents/%Y/%m/%d/')
    resume_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    feedback_update = models.CharField(choices=CANDIDATE_FEEDBACK_CHOICES, max_length=20)

    def __str__(self):
        return self.name


class ReferCandidate(models.Model):
    candidate_referrer = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="referred_candidate_by",
        null=True,
        blank=True
    )
    refer_for_the_post_of = models.ForeignKey(Jobopening, verbose_name='Referred for the post of')
    candidate_name = models.CharField(max_length=50, verbose_name='Candidate Name')
    contact_number = models.IntegerField(null=False, unique=True, verbose_name='Primary Contact Number')
    alternate_number = models.IntegerField(blank=True, verbose_name='Secondary Contact Number')
    email = models.EmailField(blank=False, unique=True, verbose_name='Email')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    current_designation = models.CharField(max_length=50, verbose_name='Present Designation')
    current_company_name = models.CharField(max_length=50, verbose_name='Current Company')
    present_location = models.CharField(choices=JOB_LOCATION_CHOICES, max_length=50, verbose_name='Present Location')
    preferred_location = models.CharField(choices=JOB_LOCATION_CHOICES, max_length=50, verbose_name='Preferred Location')
    experience = models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Experience')
    notice_period = models.CharField(choices=NOTICE_PERIOD_CHOICES, max_length=15, verbose_name='Notice Period')
    skill = models.CharField(max_length=100)
    qualification = models.CharField(choices=QUALIFICATION_CHOICES, max_length=100)
    present_salary = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    expected_salary = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    industry = models.CharField(max_length=100)
    functional_area = models.CharField(choices=FUNCTIONAL_AREA_CHOICES, max_length=100)
    employment_type = models.CharField(max_length=50)
    # resume = models.FileField(upload_to='documents/%Y/%m/%d/', null=True)
    resume_created = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.candidate_name
