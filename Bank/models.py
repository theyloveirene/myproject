from django.contrib.auth.models import User
from django.db import models

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    bank_name = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=11)
    institution_number = models.CharField(max_length=10)
    
    def _str_(self):
        return f"{self.user.username} - {self.account_number}"

class BankTransaction(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10)  # e.g., "deposit", "withdrawal"
    description = models.TextField(blank=True, null=True)
    
    def _str_(self):
        return f"{self.bank_account.account_number} - {self.transaction_type} - {self.amount}"
