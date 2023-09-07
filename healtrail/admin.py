from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name', 'desc ')

admin.site.register(Product)