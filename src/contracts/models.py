from django.db import models

from clients.models import Contact


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
