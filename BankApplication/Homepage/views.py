from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')

def Login(request):
    return render(request,'login.html')