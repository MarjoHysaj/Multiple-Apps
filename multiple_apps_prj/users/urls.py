from django.urls import path     
from . import views

urlpatterns = [
    path('register', views.index),
    path('login', views.login),
    path('users/new', views.index),
    path('user', views.user),
]