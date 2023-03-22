from django.db import models

# Modelo de cart (products puede ser array?)

class Cart(models.Model):
    username = models.CharField(max_length=100)
    products = models.CharField(max_length=100)
    creation_time = models.DateTimeField(auto_now_add=True)    