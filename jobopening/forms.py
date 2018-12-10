from django import forms
from .models import Jobopening
from jobopening.models import Jobopening, ApplicationQuestions


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


class ApplyForm(forms.Form):
    class Meta:
        model = ApplicationQuestions
        fields = '__all__'
