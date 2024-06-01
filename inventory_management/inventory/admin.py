from django.contrib import admin
from .models import Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price', 'image')  # Display the image field

admin.site.register(Category)
