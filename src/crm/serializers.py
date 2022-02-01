from rest_framework.serializers import ModelSerializer
from .models import Company, Contact, Contract, Event


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'address',
            'website',
            'notes',
            'sales_contact',
            'client'
            ]


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'mobile',
            'company'
            ]


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


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'contract',
            'support_contact',
            'finished',
            'attendees',
            'date',
            'note'
        ]
