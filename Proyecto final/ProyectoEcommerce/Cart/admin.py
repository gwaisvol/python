from django.contrib import admin

# Register your models here.
from Cart.models import Cart

# admin.site.register(Products)

@admin.register(Cart)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('username', 'products', 'creation_time')
    search_fields = ('username',)