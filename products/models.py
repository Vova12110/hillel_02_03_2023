# import os
from os import path
from django.utils.safestring import mark_safe

from django.core.validators import MinValueValidator
from django.db import models

from project1.project.constants import MAX_DIGITS, DECIMAL_PLACES
from project1.project.mixins.models import PKMixins
# from project1.settings import BASE_DIR

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# MEDIA_URL = '/media/'


def upload_to(instance, filename):
    _name, extension = path.splitext(filename)
    return f'media/media/products/images/{str(instance.pk)}{extension}'


def get_image(self, obj):
    if obj.image:
        return mark_safe(f'<img src="{obj.image.url}" width="64" height="64">')
    return ''


class Category(PKMixins):
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='media/media/products/images/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Product(PKMixins):
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='media/media/products/images/',
        null=True,
        blank=True
    )
    sku = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True)
    products = models.ManyToManyField('products.Product', blank=True)
    price = models.DecimalField(
        validators=[MinValueValidator(0)],
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES
    )

    def __str__(self):
        return f'{self.name} - {self.price}'


class Discount(models.Model):
    AMOUNT_TYPE_CHOICES = (
        (0, 'В деньгах'),
        (1, 'Проценты')
    )
    amount = models.PositiveIntegerField()
    code = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    discount_type = models.PositiveIntegerField(choices=AMOUNT_TYPE_CHOICES)
