from django.contrib import admin

# Register your models here.
# cartoon/admin.py

from django.contrib import admin
from .models import CartoonImage  # Gantilah CartoonImage dengan nama model yang sesuai

@admin.register(CartoonImage)
class CartoonImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_upload', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
