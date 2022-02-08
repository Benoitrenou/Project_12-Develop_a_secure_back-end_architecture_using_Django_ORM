from rest_framework.serializers import ModelSerializer

from clients.models import Company, Contact


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
