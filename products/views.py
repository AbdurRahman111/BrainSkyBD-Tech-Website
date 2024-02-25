from django.shortcuts import render
from .models import Product_Table
# Create your views here.


def products(request):
    all_products = Product_Table.objects.all()
    context = {'all_products':all_products}
    return render(request, 'products.html', context)


def product_details(request, slug):
    getProduct = Product_Table.objects.get(slug = slug)
    context = {'getProduct':getProduct}
    return render(request, 'product_details.html', context)
