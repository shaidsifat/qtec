# products/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def product_list(request):
    categories = request.GET.getlist('category')
    brands = request.GET.getlist('brand')
    warranties = request.GET.getlist('warranty')
    sellers = request.GET.getlist('seller')

    products = Product.objects.all()

    if categories:
        products = products.filter(category__in=categories)
    if brands:
        products = products.filter(brand__in=brands)
    if warranties:
        products = products.filter(warranty__in=warranties)
    if sellers:
        products = products.filter(seller__in=sellers)

    filtered_products = list(products.values('name'))
    return JsonResponse({'product_list': filtered_products})
