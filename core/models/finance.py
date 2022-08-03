from django.db import models

from django.contrib.auth import get_user_model
from accounts.models import UserAccount
from .firm import Firm

User = get_user_model()


class FinanceAccount(models.Model):
    owner = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name="finance_account", blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# it keeps the record of transactions of each user and return revenue in and revenue out 
class TransactionHistory(models.Model):
    to = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="transaction_to", blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    by = models.ForeignKey(User,  on_delete=models.DO_NOTHING, related_name="transaction_by", blank=True, null=True)

    is_credit = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def revenueIn(self):
        pass

    def revenueOut(self):
        pass

    def __str__(self):
        return self.user.username

