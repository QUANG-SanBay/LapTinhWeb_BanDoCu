from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('',views.get_login,name='login'),
     path('register/', views.get_register, name='register'),
     path('logout/', views.logout_view, name='logout'),
]