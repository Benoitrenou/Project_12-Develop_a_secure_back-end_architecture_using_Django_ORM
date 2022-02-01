from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Company, Contact, Contract, Event
from .serializers import CompanySerializer, ContactSerializer,\
    ContractSerializer, EventSerializer
from rest_framework.permissions import IsAuthenticated


class CompanyViewSet(ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]


class ContactViewSet(ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]


class ContractViewSet(ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]


class EventViewSet(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]