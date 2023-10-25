from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.auth_login, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout', views.auth_logout, name='logout'),

]
