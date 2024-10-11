from django import forms

from customer_invoices.invoices.models import Invoice, Item

# Source: https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024
class CustomForm(forms.ModelMultipleChoiceField):
    def label_form_instance(self, item):
        return "%s" % item.price


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        exclude = "__all__"

    item = CustomForm(
        queryset=Item.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
