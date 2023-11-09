from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('overview', views.validate, name='router'),
    path('students', views.display_students, name='r21'),
    path('update', views.update, name='update'),
    path('admin_panel',views.admin_panel,name='adminpanel'),
    path('report',views.report,name='report'),
    path('hod_panel',views.hod_panel,name='hod'),
    path('hod_view',views.hod_view,name='hod_view'),
    
    #mains
    path('login', views.auth_login, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout', views.auth_logout, name='logout'),



]

