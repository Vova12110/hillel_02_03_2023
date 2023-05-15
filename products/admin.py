from django.contrib import admin
from django.utils.safestring import mark_safe

from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image')
    readonly_fields = ('image_tag',)
    filter_horizontal = ('categories',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}"'
                             f' width="64" height="64" />')
        else:
            return 'No image'
    get_image.short_description = 'Image'

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" '
                             f'width="64" height="64" />')
        else:
            return 'No image'
    image_tag.short_description = 'Image'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
