from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MANAGEMENT = 'MANAGEMENT'
    SALES = 'SALES'
    SUPPORT = 'SUPPORT'

    ROLE_CHOICES = (
        (MANAGEMENT, 'Gestion'),
        (SALES, 'Vente'),
        (SUPPORT, 'Support'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        verbose_name='rôle',
        null=False
        )
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
