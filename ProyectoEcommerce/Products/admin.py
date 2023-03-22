from django.contrib import admin

# Register your models here.
from Products.models import Products,Categories

# admin.site.register(Products)

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_filter = ('stock',)
    search_fields = ('name',)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)