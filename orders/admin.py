from django.contrib import admin
from .models import Order, Discount, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_number', 'is_active', 'is_paid')
    list_filter = ('is_active', 'is_paid')
    search_fields = ('user__username', 'order_number')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order',
                    'product_name',
                    'quantity',
                    'price',
                    'discount_type',
                    'discount_value')
    list_filter = ('order',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount_type', 'value', 'description')
