# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm



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

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'app/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'app/post_edit.html', {'form': form})