from django.contrib import admin
from django.urls import path
from .views import Home,About,Login,Logout,Signup,deposit,withdraw,balance

urlpatterns = [
    path('', Home,name="home"),
    path('about', About,name="about"),
    path('login', Login,name="login"),
    path('signup', Signup,name="signup"),
    path('logout', Logout,name="logout"),
    path('deposit', deposit,name="deposit"),
    path('withdraw', withdraw,name='withdraw'),
    path('balance', balance,name='balance'),
]