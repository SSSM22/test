from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf import settings
from django.urls import re_path
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('', views.index, name='index'),
    path('overview', views.validate, name='router'),
    path('students', views.display_students, name='r21'),
    path('update', views.update, name='update'),
    path('admin_panel',views.admin_panel,name='adminpanel'),
    path('report',views.report,name='report'),
    path('hod_panel',views.hod_panel,name='hod'),
    path('hod_view',views.hod_view,name='hod_view'),
    path('student_view/<str:username>/',views.student_view,name='student_view'),
    path('change_password',views.change_password,name='change_password'),
    path('usernames', views.usernames, name='usernames'),
    path('update_usernames',views.update_usernames,name='update_usernames'),
    path('login', views.auth_login, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout', views.auth_logout, name='logout'),
    path('load_rows', views.load_rows, name="load_rows"),
    path('principal_view', views.principal_view, name="principal_view")


]

