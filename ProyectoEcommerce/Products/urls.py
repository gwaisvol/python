from django.urls import path

from Products.views import create_product, list_products, create_category, list_categories


urlpatterns = [
    path('create-product/', create_product),
    path('list-products/', list_products),
    path('create-category/', create_category),
    path('list-categories/', list_categories),

]