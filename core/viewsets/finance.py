from rest_framework import viewsets, permissions
from core.models.finance import FinanceAccount, TransactionHistory
from core.serializers.finance import FinanceAccountSerializer, TransactionHistorySerializer

class FinanceAccountViewsets(viewsets.ModelViewSet):
    queryset = FinanceAccount.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FinanceAccountSerializer

class TransactionHistoryViewsets(viewsets.ModelViewSet):
    queryset = TransactionHistory.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TransactionHistorySerializer
    