from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register_view, name='register'),
    path('login/', views.Login_view, name='login'),
    path('logout/', views.Logout_view, name='logout'),
]