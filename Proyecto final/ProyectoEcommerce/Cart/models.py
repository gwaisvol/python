from django.db import models
from Products.models import Products

list_of_products = Products.objects.all()
CHOICES = []

class Cart(models.Model): 
    for prod in list_of_products:
        CHOICES.append((prod.name, prod.name),)

    tuple_of_products = tuple(CHOICES)  
    username = models.CharField(max_length=100)
    products = models.CharField(choices=CHOICES, max_length=90)
    creation_time = models.DateTimeField(auto_now_add=True)    