from django.contrib import admin
from .models import Company, Contact

class ContactInLine(admin.TabularInline):

    model = Contact


class CompanyAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'sales_contact',
        'client',
        )
    inlines = [ContactInLine]
    search_fields = ['name__startswith']


admin.site.register(Company, CompanyAdmin)
