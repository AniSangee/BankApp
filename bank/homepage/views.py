from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from .forms import DepositForm, TransferForm
from .models import BankAccount, Transaction
from django.contrib.auth.decorators import login_required

def Home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            BankAccount.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

# logout
def Logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    account = BankAccount.objects.get(user=request.user)
    transactions = Transaction.objects.filter(from_account=account)
    return render(request, 'dashboard.html', {'account': account, 'transactions': transactions})

@login_required
def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            account = BankAccount.objects.get(user=request.user)
            account.balance += amount
            account.save()
            Transaction.objects.create(from_account=account, amount=amount, transaction_type='Deposit')
            return redirect('dashboard')
    else:
        form = DepositForm()
    return render(request, 'deposit.html', {'form': form})

@login_required
def transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            to_account_id = form.cleaned_data['to_account']
            account = BankAccount.objects.get(user=request.user)
            to_account = BankAccount.objects.get(id=to_account_id)
            if account.balance >= amount:
                account.balance -= amount
                to_account.balance += amount
                account.save()
                to_account.save()
                Transaction.objects.create(from_account=account, to_account=to_account, amount=amount, transaction_type='Transfer')
                return redirect('dashboard')
    else:
        form = TransferForm()
    return render(request, 'transfer.html', {'form': form})

from django.contrib import messages
from .models import BankAccount,Transaction
from .forms import WithdrawalForm
@login_required
def withdraw_view(request):
    account = BankAccount.objects.get(user=request.user)
    if request.method == "POST":
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if amount > account.balance:
                messages.error(request, "Insufficient balance.")
            else:
                account.balance -= amount
                account.save()
                
                # Record the transaction
                Transaction.objects.create(
                    account=account,
                    transaction_type="Withdrawal",
                    amount=amount
                )
                
                messages.success(request, f"${amount} withdrawn successfully!")
                return redirect('dashboard')  # Redirect to dashboard or any other page
    else:
        form = WithdrawalForm()

    return render(request, 'withdraw.html', {'form': form, 'balance': account.balance})
