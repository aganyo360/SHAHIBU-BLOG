# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'app/register.html', {'form': form})

def login_view(request):
    return auth_views.LoginView.as_view(template_name='app/login.html')(request)


def logout_view(request):
    logout(request)
    return redirect('home')
def home(request):
    return render(request, 'app/home.html')