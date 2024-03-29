from django.db import models

# Modelos de productos y categorias
class Products(models.Model):
    image = models.ImageField(upload_to='products_images', null=True, blank=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=50, default="General")
    stock = models.BooleanField(default=False)

class Categories(models.Model):
    name = models.CharField( max_length=20, unique=True)
