from rest_framework.serializers import ModelSerializer

from contracts.models import Contract


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'id',
            'client',
            'signed_status',
            'amount',
            'payment_due'
        ]
