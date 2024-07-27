from django.urls import path
from . import views

app_name = 'bank'

urlpatterns = [
    path('accounts/', views.bank_account_list, name='bank_account_list'),
    path('accounts/<int:account_id>/add_transaction/', views.add_transaction, name='add_transaction'),
]