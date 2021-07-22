from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *


#login cyrcle views


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:overview')
    return HttpResponse('<div style="display: inline-block; padding:5em;"><h1 style="text-align: center; padding:2em; font-size: 2rem;">Your username or password is wrong check it out and try again!<br>If you do not know the username, password or you do not have the Login send an email to <span style="color: purple;">admin@horizon-development.com</span></h1><br><a style="width: 10em; height:2.5empx; padding: .5em; cursor: pointer; font-size: 2rem; background: red; border-radius: 20px; color: #fff; text-decoration: none;" href="/">Return</a></div>')


def logoutPage(request):
    logout(request)
    return redirect('pages:home')

def updatePage(request):
    pass





