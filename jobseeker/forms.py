from django import forms

from .models import Jobseeker, ReferCandidate


class ResumeSubmitForm(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = '__all__'
        exclude = ('resume_created',)


class ReferCandidateForm(forms.ModelForm):
    class Meta:
        model = ReferCandidate
        fields = ['refer_for_the_post_of', 'candidate_name', 'contact_number', 'alternate_number', 'email', 'gender',
                  'current_designation',
                  'current_company_name', 'present_location', 'preferred_location', 'experience', 'notice_period',
                  'skill', 'qualification', 'present_salary', 'expected_salary', 'industry', 'functional_area',
                  'employment_type', ]

        exclude = ('resume_created',)
