from django.contrib import admin
from .models import Contract


class ContractAdmin(admin.ModelAdmin):

    list_display = (
        'client',
        'signed_status',
        'amount',
        'payment_due'
    )
    list_filter = (
        'client',
        'client__company',
        'client__company__sales_contact',
    )


admin.site.register(Contract, ContractAdmin)
