from django.conf import settings
from django.db import models

from contracts.models import Contract


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
