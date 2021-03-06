from rest_framework.viewsets import ModelViewSet

from clients.models import Company, Contact
from clients.serializers import CompanySerializer, ContactSerializer
from clients.permissions import HasClientPermissions
from rest_framework.permissions import IsAuthenticated


class CompanyViewSet(ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [
        IsAuthenticated,
        HasClientPermissions
        ]
    filterset_fields = [
        'name',
        'sales_contact',
        ]


class ContactViewSet(ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [
        IsAuthenticated,
        HasClientPermissions
        ]
