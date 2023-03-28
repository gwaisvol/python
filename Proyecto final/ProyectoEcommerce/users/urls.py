from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import login_user,register, update_user_profile


urlpatterns = [
    path('login/', login_user),
    path('logout/', LogoutView.as_view(template_name = 'logout/logout.html')),
    path('signup/', register),
    path('update-profile/', update_user_profile)
]