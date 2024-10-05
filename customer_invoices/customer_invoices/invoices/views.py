from neapolitan.views import CRUDView

from customer_invoices.invoices.models import Customer, Item, Invoice


class CustomerView(CRUDView):
    model = Customer
    fields = ["first_name", "last_name", "city", "email", "address"]


class ItemView(CRUDView):
    model = Item
    fields = ["name", "quantity", "price"]


class InvoiceView(CRUDView):
    model = Invoice
    fields = ["item", "customer", "total_items", "total_price", "date", "expiry_date", "done"]
    filterset_fields = [
        "customer",
        "done"
    ]
