from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AuthenticationForm
from django.http import HttpResponse
# Create your views here.


def loginView(request):
    context = {
    }
    user = request.user
    if user.is_authenticated:
        return redirect('homepage')
    if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    context['login_form'] = form
    return render(request, 'accounts/loginPage.html', context)


def signupView(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('homepage')
        else:
            context['registration_form'] = form
    else:  # GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/signupPage.html', context)


def logoutView(request):
    logout(request)
    return redirect('homepage')
