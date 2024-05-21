from django.contrib import admin
from .models import ProductModel

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Desc')
admin.site.register(ProductModel, ProductAdmin)