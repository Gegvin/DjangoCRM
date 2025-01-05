from django.db import models
from django.utils import timezone

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Order(models.Model):
    COFFEE_CHOICES = [
        ('espresso', 'Espresso'),
        ('latte', 'Latte'),
        ('cappuccino', 'Cappuccino'),
        ('americano', 'Americano'),
    ]
    SYRUP_CHOICES = [
        ('vanilla', 'Vanilla'),
        ('caramel', 'Caramel'),
        ('hazelnut', 'Hazelnut'),
        ('none', 'No Syrup'),
    ]

    # Цены для кофе и сиропов
    COFFEE_PRICES = {
        'espresso': 2.5,
        'latte': 3.0,
        'cappuccino': 3.5,
        'americano': 2.8,
    }

    SYRUP_PRICES = {
        'vanilla': 0.5,
        'caramel': 0.5,
        'hazelnut': 0.6,
        'none': 0.0,
    }

    order_number = models.CharField(max_length=20, unique=True, blank=True)
    coffee = models.CharField(max_length=20, choices=COFFEE_CHOICES)
    syrup = models.CharField(max_length=20, choices=SYRUP_CHOICES)
    status = models.BooleanField(default=False)  # False = Не оплачено, True = Оплачено
    created_at = models.DateTimeField(auto_now_add=True)

    # Новые поля для хранения цен
    coffee_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    syrup_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        if not self.order_number:
            now = timezone.now()
            month_year = now.strftime('%m%y')  # Формат MMYY, например, '0125'
            # Получаем количество заказов в текущем месяце
            count = Order.objects.filter(
                created_at__year=now.year,
                created_at__month=now.month
            ).count() + 1
            self.order_number = f"{count}-{month_year}"

        # Устанавливаем цены на основе выбора
        self.coffee_price = self.COFFEE_PRICES.get(self.coffee, 0.0)
        self.syrup_price = self.SYRUP_PRICES.get(self.syrup, 0.0)
        self.total_price = self.coffee_price + self.syrup_price

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number