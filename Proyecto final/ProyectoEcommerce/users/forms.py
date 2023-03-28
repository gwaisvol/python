from django import forms
from users.models import UserProfile

class UserProfileForm(forms.Form):
   CHOICES = (
         ('-','-'),
         ('Masculino', 'Masculino'),
         ('Femenino', 'Femenino'),
         ('Otro', 'Otro'),
    )
   phone = forms.CharField(max_length=100, label="Telefono", required=True)
   date_of_birth = forms.CharField(label="Fecha de nacimiento",required=False)
   gender = forms.ChoiceField(choices=CHOICES, label="Genero",required=True)
   avatar = forms.ImageField(required=False)
   