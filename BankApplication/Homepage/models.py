from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s account"

    def deposit(self, amount):
        self.balance += amount
        self.save()
        Transaction.objects.create(account=self, amount=amount, transaction_type='deposit')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            Transaction.objects.create(account=self, amount=amount, transaction_type='withdraw')
        else:
            raise ValueError("Insufficient funds")

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(default=timezone)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} - {self.amount} on {self.timestamp}"
