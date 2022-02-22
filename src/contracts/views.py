from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from contracts.models import Contract
from contracts.permissions import HasContractPermissions
from contracts.serializers import ContractSerializer


class ContractViewSet(ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [
        IsAuthenticated,
        HasContractPermissions
        ]
    filterset_fields = [
        'client',
        'client__company__sales_contact',
        'signed_status',
        'payment_due'
        ]
