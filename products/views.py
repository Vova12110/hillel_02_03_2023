from django.shortcuts import render, get_object_or_404
from products.models import Product


def products(request):
    return render(request, 'products/index.html', {'message': 'Товары'})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
