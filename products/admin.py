from django.contrib import admin
from products.models import ProductCategory, Product 

# Register models

admin.site.register(Product)
admin.site.register(ProductCategory)