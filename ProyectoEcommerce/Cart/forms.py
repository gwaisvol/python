from django import forms

class CartForm(forms.Form):
    username = forms.CharField(max_length=100, label="Usuario")
    products = forms.CharField(max_length=100, label="Productos")
