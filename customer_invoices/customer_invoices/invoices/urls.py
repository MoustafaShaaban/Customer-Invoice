from django.urls import path

from customer_invoices.invoices.views import CustomerView, ItemView, InvoiceView, create_invoice, CreateInvoiceView


urlpatterns = [
    path('create-invoice/', CreateInvoiceView.as_view(), name='create-invoice'),
    #path('create_invoice_function/', create_invoice, name='create-invoice-function'),
    *CustomerView.get_urls(),
    *ItemView.get_urls(),
    *InvoiceView.get_urls(),
]
