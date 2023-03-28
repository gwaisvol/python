from django.urls import path

from Cart.views import create_cart,list_of_carts


urlpatterns = [
    path('cart/', create_cart),
    path('list-of-carts/', list_of_carts),

]