from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):

    list_display = (
        'contract',
        'support_contact',
        'finished',
        'date',
        'attendees'
    )


admin.site.register(Event, EventAdmin)
