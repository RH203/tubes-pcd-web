# scanner/forms.py

from django import forms
from .models import ScannerImage

class ScannerImageForm(forms.ModelForm):
    class Meta:
        model = ScannerImage
        fields = ['title', 'image_upload']
