from django.contrib import admin
from .models import User


class CustomUserAdmin(admin.ModelAdmin):
    """
    Customization of the UserAdmin class in order to make it call a
    personalized form for the creation of a new user
    """
    list_display = (
        'pk',
        'username',
        'first_name',
        'last_name',
        'role',
        'email',
        'phone',
        'mobile',
        'date_created',
        'date_updated'
        )
    list_filter = (
        'role',
        'last_name',
    )


admin.site.register(User, CustomUserAdmin)
