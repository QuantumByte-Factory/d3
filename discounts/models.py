# discounts/models.py
from django.db import models
from stores.models import Store  

class Discount(models.Model):
    title = models.CharField(max_length=255)
    initial_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='discounts')
    image = models.ImageField(upload_to='discount_images/')
    expiry_date = models.DateField()

    @property
    def price_after_discount(self):
        discount_amount = (self.discount_percentage / 100) * self.initial_price
        return self.initial_price - discount_amount

    def __str__(self):
        return f"{self.title} - {self.store.name}"
