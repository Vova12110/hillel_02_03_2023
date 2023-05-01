# from os import path
import uuid

from django.db import models


# def upload_to(instance, filename):
#     _name, extension = path.splitext(filename)
#     return f'products/images/{str(instance.pk)}{extension}'


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True
    )
    # image = models.ImageField(upload_to=upload_to)
    sku = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField(upload_to='category_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Discount(models.Model):
    AMOUNT_TYPE_CHOICES = (
        (0, 'В деньгах'),
        (1, 'Проценты')
    )
    amount = models.PositiveIntegerField()
    code = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    discount_type = models.PositiveIntegerField(choices=AMOUNT_TYPE_CHOICES)
