from django import forms

from .models import Jobseeker, ReferCandidate, Jobopening


class ResumeSubmitForm(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = '__all__'
        exclude = ('resume_created', 'feedback_update')


class ReferCandidateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ReferCandidateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ReferCandidate
        fields = ['refer_for_the_post_of', 'candidate_name', 'contact_number', 'alternate_number', 'email', 'gender',
                  'current_designation',
                  'current_company_name', 'present_location', 'preferred_location', 'experience', 'notice_period',
                  'skill', 'qualification', 'present_salary', 'expected_salary', 'industry', 'functional_area',
                  'employment_type', ]

        exclude = ('resume_created',)

    def save(self, commit=True):
        obj = super(ReferCandidateForm, self).save(commit=False)

        if obj.user is None:
            obj.user = self.user

        if commit:
            obj.save()
        return obj
