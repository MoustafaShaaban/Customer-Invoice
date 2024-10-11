from django.http import HttpResponseRedirect
from django.shortcuts import render

from neapolitan.views import CRUDView

from customer_invoices.invoices.models import Customer, Item, Invoice
from customer_invoices.invoices.forms import InvoiceForm


def create_invoice(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = InvoiceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InvoiceForm()

    return render(request, "invoices/create_invoice_function.html", {"form": form})



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
