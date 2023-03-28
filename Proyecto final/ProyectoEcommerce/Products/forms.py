from django import forms

class ProductForm(forms.Form):
    image = forms.ImageField(label="Imagen",required=False)
    name = forms.CharField(max_length=100, label="Nombre")
    price = forms.FloatField(label="Precio")
    category = forms.CharField(max_length=50, label="Categoria")
    stock = forms.BooleanField(required=False)

class CategoriesForm(forms.Form):
    name = forms.CharField(max_length=50, label="Nombre")