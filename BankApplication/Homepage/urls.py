from django.contrib import admin
from django.urls import path
from .views import Home,About,Login

urlpatterns = [
    path('', Home,name="home"),
    path('about', About,name="about"),
    path('login', Login,name="login"),
]
