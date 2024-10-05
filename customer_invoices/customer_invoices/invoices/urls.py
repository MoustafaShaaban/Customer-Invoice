from django.urls import path

from customer_invoices.invoices.views import CustomerView, ItemView, InvoiceView


urlpatterns = [
    *CustomerView.get_urls(),
    *ItemView.get_urls(),
    *InvoiceView.get_urls(),
]
