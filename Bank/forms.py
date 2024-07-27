from django import forms
from .models import BankTransaction

class BankTransactionForm(forms.ModelForm):
    class Meta:
        model = BankTransaction
        fields = ['amount', 'transaction_type', 'description']