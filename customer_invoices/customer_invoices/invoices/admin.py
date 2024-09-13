from django.contrib import admin

from customer_invoices.invoices.models import Customer, Item, Invoice
# Register your models here.
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Invoice)
