from django.db import models
from epicevents_crm import settings


class Company(models.Model):

    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=255)
    website = models.CharField(max_length=100)
    notes = models.TextField()
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='clients',
        on_delete=models.SET_NULL,
        null=True
    )
    client = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)


class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    company = models.ForeignKey(
        to=Company,
        related_name='contacts',
        on_delete=models.CASCADE
        )


class Contract(models.Model):

    client = models.ForeignKey(
        to=Contact,
        related_name='contracts',
        on_delete=models.CASCADE
        )
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    signed_status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateField()


class Event(models.Model):

    contract = models.ForeignKey(
        to=Contract,
        related_name='event',
        on_delete=models.CASCADE
        )
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='events',
        on_delete=models.SET_NULL,
        null=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    finished = models.BooleanField(default=False)
    attendees = models.IntegerField()
    date = models.DateField()
    notes = models.TextField()