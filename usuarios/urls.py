from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name="register"),
]
