from django.urls import path

from customer_invoices.invoices.views import CustomerView, ItemView, InvoiceView, create_invoice


urlpatterns = [
    path('create_invoice_function/', create_invoice, name='create-invoice-function'),
    *CustomerView.get_urls(),
    *ItemView.get_urls(),
    *InvoiceView.get_urls(),
]
