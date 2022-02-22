from django.contrib import admin
from .models import Company, Contact

class ContactInLine(admin.TabularInline):

    model = Contact


class CompanyAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'sales_contact',
        'client',
        'date_created',
        'date_updated'
        )
    list_filter = (
        'name',
        'sales_contact',
    )
    inlines = [ContactInLine]
    search_fields = ['name__startswith']

admin.site.register(Company, CompanyAdmin)
