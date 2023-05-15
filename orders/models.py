from django.db import models
from django.contrib.auth.models import User


class Discount(models.Model):
    DISCOUNT_TYPES = (
        ('percent', 'Проценты'),
        ('amount', 'Сумма'),
    )
    name = models.CharField(max_length=255)
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPES)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.PositiveIntegerField()
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    def get_total_price_with_discount(self):
        total_price = 0
        for item in self.items.all():
            item_price = item.price
            if item.discount_type:
                if item.discount_type == 'percent':
                    item_price = item.price * (100 - item.discount_value) / 100
                else:
                    item_price = item.price - item.discount_value
            total_price += item_price * item.quantity
        if self.discount:
            if self.discount.discount_type == 'percent':
                total_price *= (100 - self.discount.value) / 100
            else:
                total_price -= self.discount.value
        return total_price


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_type = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=Discount.DISCOUNT_TYPES
    )
    discount_value = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )

    def get_price_with_discount(self):
        price = self.price
        discount_type = self.discount_type
        discount_value = self.discount_value

        if discount_type == 'percent':
            price -= price * (discount_value / 100)
        elif discount_type == 'amount':
            price -= discount_value

        return price * self.quantity
