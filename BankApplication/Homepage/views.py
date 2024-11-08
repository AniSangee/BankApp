from django.shortcuts import render,redirect

# Create your views here.
def Home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')

# loginpage
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

def Login(request):
    if request.method == 'POST':
        form= AuthenticationForm(request,data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user =authenticate(username = username, password = password) 
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return render(request,'login.html',{'form':form})
    else:
        form=AuthenticationForm()
    
    return render(request,'login.html',{'form':form})
# signup
def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
         form = UserCreationForm()
    return render(request,'signup.html',{'form':form})
# logout
def Logout(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Account

@login_required
def deposit(request):
    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        account = get_object_or_404(Account, user=request.user)
        account.deposit(amount)
        messages.success(request, f"{amount} deposited successfully!")
        return redirect("balance")
    return render(request, "bank/deposit.html")

@login_required
def withdraw(request):
    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        account = get_object_or_404(Account, user=request.user)
        try:
            account.withdraw(amount)
            messages.success(request, f"{amount} withdrawn successfully!")
        except ValueError as e:
            messages.error(request, str(e))
        return redirect("balance")
    return render(request, "bank/withdraw.html")

@login_required
def balance(request):
    account = get_object_or_404(Account, user=request.user)
    transactions = account.transactions.all().order_by('-timestamp')
    return render(request, "bank/balance.html", {"account": account, "transactions": transactions})


