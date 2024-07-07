from django import forms

class ProductForm(forms.Form):
    name = forms.TextField(max_length=200, label="Nombre")
    description = forms.TextField(max_length=300, label="Descripción")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available=forms.BooleanField(initial=True, label="Disponble", required=False)
    photo = forms.ImageField(label="Foto", required=False)