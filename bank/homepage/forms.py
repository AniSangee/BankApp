from django import forms

class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class TransferForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    to_account = forms.IntegerField()

class WithdrawalForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Withdrawal Amount",
        min_value=0.01,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount to withdraw'})
    )