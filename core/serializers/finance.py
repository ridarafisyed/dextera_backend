from  core.models.finance  import FinanceAccount, TransactionHistory


from rest_framework import serializers

class FinanceAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model= FinanceAccount
        fields= ("id", "owner", "balance")

class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model= TransactionHistory
        fields= ("id", # need to do a better job in transaction and bankaccount 
                "to",
                "amount",
                "by",
                "is_credit",
                "created_at")

        