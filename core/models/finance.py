from django.db import models

from django.contrib.auth import get_user_model

from .firm import Firm

User = get_user_model()
TRANS_CHOICES = [
    ("cd", 'Credit'),
    ("db", 'Debit'),
   
]

# it keeps the record of transactions of each user and return revenue in and revenue out 
class TransactionHistory(models.Model):
    to = models.ForeignKey(Firm, on_delete=models.DO_NOTHING, related_name="transaction_to", blank=True, null=True)
    amount = models.DecimalField()
    by = models.ForeignKey(User,  on_delete=models.DO_NOTHING, related_name="transaction_by", blank=True, null=True)
    is_credit = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def revenueIn(self):
        pass

    def revenueOut(self):
        pass

    def __str__(self):
        return self.user.username
