from django.urls import path
from .views import  Home,About,register,login_view,Logout,dashboard,deposit, transfer,withdraw_view

urlpatterns = [
    path('', Home,name="home"),
    path('about', About,name="about"),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', Logout,name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('deposit/', deposit, name='deposit'),
    path('transfer/', transfer, name='transfer'),
    path('withdraw/', withdraw_view, name='withdraw'),
]
