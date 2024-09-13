from django.db import models

# Create your models here.
class Customer(models.Model):
    """Model definition for Customer."""

    # TODO: Define fields here
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    job = models.CharField(max_length=100)


    class Meta:
        """Meta definition for Customer."""

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table = 'Customer'

    def __str__(self):
        """Unicode representation of Customer."""
        return f"{self.first_name}"


    # def get_absolute_url(self):
    #     """Return absolute url for Customer."""
    #     return ('')

# Create your models here.
class Item(models.Model):
    """Model definition for Item."""

    # TODO: Define fields here
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)


    class Meta:
        """Meta definition for Item."""

        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        db_table = 'Item'

    def __str__(self):
        """Unicode representation of Item."""
        return self.name


    # def get_absolute_url(self):
    #     """Return absolute url for Item."""
    #     return ('')


class Invoice(models.Model):
    """Model definition for Invoice."""

    # TODO: Define fields here
    item = models.ManyToManyField(Item)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    expiry_date = models.DateField()
    done = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Invoice."""

        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        """Unicode representation of Invoice."""
        return self.customer
