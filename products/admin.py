from django.contrib import admin
from .models import Product,Seller,Warranty,Brand,Category


# Register your models here.
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Warranty)
admin.site.register(Brand)
admin.site.register(Category)