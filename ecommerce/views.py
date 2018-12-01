from django.contrib.auth import authenticate, login, get_user_model
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView

from employer.models import CompanyProfile
from jobopening.models import Jobopening
from jobseeker.models import Jobseeker
from .forms import ContactForm, LoginForm, RegisterForm



def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Us !!",
        "content": "Welcome to Contact Page.",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact.html", context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }
    print("User Logged in")
    print(request.user.is_authenticated())
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated())
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            # redirect to success page.
            context['form'] = LoginForm()
            return redirect("/login")
        else:
            print("Error")

    return render(request, 'auth/login_page.html', context)


User = get_user_model()


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "form": register_form
    }
    if register_form.is_valid():
        print(register_form.cleaned_data)
        username = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")

        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, 'auth/register_page.html', context)


from django.views.generic import ListView


