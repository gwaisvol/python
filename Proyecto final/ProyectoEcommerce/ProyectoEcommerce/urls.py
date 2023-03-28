from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from ProyectoEcommerce.settings import MEDIA_ROOT, MEDIA_URL

from ProyectoEcommerce.views import welcome_page,our_company
from users.views import login_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_page),
    path('home', welcome_page),
    path('nosotros', our_company),
    path('Products/', include('Products.urls')),
    path('cart/', include('Cart.urls')),
    path('user/', include('users.urls'))

]+ static(MEDIA_URL, document_root = MEDIA_ROOT)
