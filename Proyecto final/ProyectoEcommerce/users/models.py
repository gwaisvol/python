from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=25, null=True, blank=True)
    date_of_birth = models.CharField(null=True, blank=True, max_length=15)
    gender = models.CharField(choices=CHOICES, max_length=14,null=True, blank=True) 
    avatar = models.ImageField(upload_to='profile_images', null=True, blank=True)

