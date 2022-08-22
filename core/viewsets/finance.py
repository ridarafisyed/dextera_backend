from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.response import Response
from ..models.firm import Firm
from core.models.finance import FinanceAccount, Subscription, TransactionHistory
from core.serializers.finance import FinanceAccountSerializer, IsSubscriptionActiveSerializer, SubscriptionSerializer, TransactionHistorySerializer
from accounts.models import UserAccount
class FinanceAccountViewsets(viewsets.ModelViewSet):
    queryset = FinanceAccount.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FinanceAccountSerializer


class IsSubscriptionViewset(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IsSubscriptionActiveSerializer

    def get_queryset(self):
    
        queryset = Subscription.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = Subscription.objects.filter(user=user)
        return queryset

class SubscriptionViewset(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = SubscriptionSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        finacne = FinanceAccount.objects.get_or_create(owner = self.request.user.id)
        admin = UserAccount.objects.get(is_superuser = True)
        finacne = FinanceAccount.objects.get(owner = admin)

        if serializer.is_valid():
            subscription = serializer.save()
            subscription.is_active = True
            finacne.balance -= serializer.validated_data['amount']
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Subscription.objects.all()
        user = self.request.query_params.get('user')
        
        if user is not None:
            queryset = Subscription.objects.filter(user=user)
        return queryset

class TransactionHistoryViewsets(viewsets.ModelViewSet):
    queryset = TransactionHistory.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TransactionHistorySerializer
    
