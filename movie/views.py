from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import CreateUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def register_user(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username') + ' successfully')
            return redirect('login')
    context = {'form':form}
    return render(request, 'movie/register.html',context)

def login_user(request):
    form = LoginForm()
    context = {'form':form}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'movie/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    user = User
    if user is not None:
        messages.success(request, 'You are logged in')
        return render(request, 'movie/index.html')
    else:
        messages.info(request, 'Please login to continue')
        return render(request, 'movie/login.html')