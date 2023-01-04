from django.contrib import admin
from products.models import ProductCategory, Product 

# Register models

# admin.site.register(Product)
admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'quantity', 'category')
  fields = ('name', 'description', 'price', 'quantity', 'image', 'category')
  search_fields = ('name',)
  ordering = ('-name',)