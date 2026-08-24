from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
]
