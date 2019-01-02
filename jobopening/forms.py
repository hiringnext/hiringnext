from django import forms
from django.contrib.admin.widgets import AdminDateWidget

import jobseeker
from ecommerce.choice.experience import EXPERIENCE_CHOICE
from ecommerce.choice.job_location import JOB_LOCATION_CHOICES
from ecommerce.choice.notice_period import NOTICE_PERIOD_CHOICES
from ecommerce.choice.qualification import QUALIFICATION_CHOICES
from .models import Jobopening
from jobopening.models import Jobopening, ApplicationQuestions
from django import forms


class JobopeningForm(forms.ModelForm):
    class Meta:
        model = Jobopening
        fields = '__all__'
        exclude = ('job_created',)


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control",
               "id": "form_full_name",
               "placeholder": "Your Full Name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control",
               "id": "form_full_name",
               "placeholder": "Your Email ID"}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control",
               "id": "form_full_name",
               "placeholder": "Your Content Here."}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be 'gmail.com'")
        return email
#
#
# class ReferCandidateForm(forms.ModelForm):
#     class Meta:
#         model = jobseeker
#         fields = '__all__'
#         exclude = ('apply_for_the_post_of','feedback_update', 'resume_created')


class JobApplyForm(forms.Form):
    qualification = forms.ChoiceField(choices=QUALIFICATION_CHOICES)
    total_experience = forms.ChoiceField(choices=EXPERIENCE_CHOICE)
    relevant_experience = forms.ChoiceField(choices=EXPERIENCE_CHOICE)
    present_location = forms.ChoiceField(choices=JOB_LOCATION_CHOICES)
    present_company = forms.CharField(max_length=100)
    present_designation = forms.CharField(max_length=100)
    present_salary = forms.DecimalField(max_digits=3)
    expected_salary = forms.DecimalField(max_digits=3)
    notice_period = forms.ChoiceField(choices=NOTICE_PERIOD_CHOICES)
    Location_issue = forms.BooleanField(required=False)
    available_for_interview = forms.DateField(widget=AdminDateWidget)

