# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/new/', views.post_new, name='post_new'),
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
