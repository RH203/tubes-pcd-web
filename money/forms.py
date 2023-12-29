from django import forms
from .models import MoneyImage

class MoneyImageForm(forms.ModelForm):
    class Meta:
        model = MoneyImage
        fields = ['title', 'image_upload']
