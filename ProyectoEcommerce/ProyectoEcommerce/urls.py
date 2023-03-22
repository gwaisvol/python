from django.contrib import admin
from django.urls import path,include

from ProyectoEcommerce.views import welcome_page,our_company
""" from Products.views import create_product,list_products
 """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_page),
    path('home', welcome_page),
    path('nosotros', our_company),
    path('Products/', include('Products.urls')),
    path('cart/', include('Cart.urls'))
]
