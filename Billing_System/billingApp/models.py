from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    product_id = models.CharField(max_length=100, unique=True)
    available_stocks = models.PositiveIntegerField()
    unit_price= models.FloatField()
    tax_percentage = models.FloatField()

    def __str__(self):
        return self.name

    def total_price(self):
        return self.unit_price * (1 + self.tax_percentage / 100)
    class Meta:
        db_table ="Product"

class BillInfo(models.Model):
    customer_email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill {self.id} - {self.customer_email}"

