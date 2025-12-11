from django import forms
from .models import Product, Catalogue

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']


class CatalogueForm(forms.ModelForm):
    class Meta:
        model = Catalogue
        fields = ['name', 'telephone', 'address', 'email']

    # Optional: extra validation for telephone
    def clean_telephone(self):
        tel = self.cleaned_data.get('telephone')
        if not tel.isdigit():
            raise forms.ValidationError("Telephone must contain only numbers")
        return tel
