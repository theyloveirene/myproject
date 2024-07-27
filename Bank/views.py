from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BankAccount, BankTransaction
from .forms import BankTransactionForm

def bank_account_list(request):
    accounts = BankAccount.objects.filter(user=request.user)
    return render(request, 'bank/bank_account_list.html', {'accounts': accounts})

def add_transaction(request, account_id):
    account = get_object_or_404(BankAccount, id=account_id)
    if request.method == 'POST':
        form = BankTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.bank_account = account
            transaction.save()
            return HttpResponseRedirect(reverse('bank:bank_account_list'))
    else:
        form = BankTransactionForm()
    return render(request, 'bank/add_transaction.html', {'form': form, 'account': account})

