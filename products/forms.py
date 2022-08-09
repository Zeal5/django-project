from turtle import title
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = [
        #     'title',
        #     'description', 
        #     'price',
        # ]

class RawProductForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField()
    price       = forms.DecimalField()
