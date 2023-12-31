from django import forms
from .models import CartoonImage

class CartoonImageForm(forms.ModelForm):
    class Meta:
        model = CartoonImage
        fields = ['title', 'image_upload']
