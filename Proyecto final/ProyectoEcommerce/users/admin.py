from django.contrib import admin
from users.models import UserProfile

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'date_of_birth', 'gender', 'avatar')
  
