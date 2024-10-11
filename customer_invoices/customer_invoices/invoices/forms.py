from django import forms

from customer_invoices.invoices.models import Invoice, Item

# Source: https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024
# class CustomForm(forms.ModelMultipleChoiceField):
#     def label_form_instance(self, item):
#         return "%s" % item.price


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'item': forms.CheckboxSelectMultiple(),
        }

    # item = CustomForm(
    #     queryset=Item.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )
