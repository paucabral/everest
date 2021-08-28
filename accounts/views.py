from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import CreateUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='accounts/login.html', context={})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin')
            else:
                return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect.')
        return render(request, template_name='accounts/login.html', context={})


class Register(View):
    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        return render(request, template_name='accounts/register.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            profile = Profile(user=user)
            profile.save()
            return redirect('/registration-success/')

        else:
            messages.error(request, 'There was an error.')
        return render(request, template_name='accounts/register.html', context={'form': form})


class RegistrationSuccess(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='accounts/registration-success.html', context={})
