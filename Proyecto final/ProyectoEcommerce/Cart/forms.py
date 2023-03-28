from django import forms
from Products.models import Products

list_of_products = Products.objects.all()
CHOICES = []

class CartForm(forms.Form): 
    for prod in list_of_products:
        CHOICES.append((prod.name, prod.name),)

    tuple_of_products = tuple(CHOICES)
    products = forms.ChoiceField(choices=tuple_of_products, label="Productos",required=True)
