# analytics/models.py

from django.db import models

class OrderAnalytics(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    coffee = models.CharField(max_length=20)
    syrup = models.CharField(max_length=20)
    coffee_price = models.DecimalField(max_digits=5, decimal_places=2)
    syrup_price = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number