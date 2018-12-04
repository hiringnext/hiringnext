from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


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

    def save(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save(request)
        return

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email

    def clean_fullname(self):
        fullname = self.cleaned_data.get("fullname")
        return fullname

    def clean_contact(self):
        contact = self.cleaned_data.get("contact")
        return contact


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control",
               "id": "User Name",
               "placeholder": "User Name"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control",
               "id": "Password",
               "placeholder": "Password"}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control",
               "id": "User Name",
               "placeholder": "User Name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control",
               "id": "form_full_name",
               "placeholder": "Your Email ID"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control",
               "id": "Password",
               "placeholder": "Password"}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={"class": "form-control",
               "id": "Password",
               "placeholder": "Confirm Password"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken.")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password != password:
            raise forms.ValidationError("Password must match.")
        return data
