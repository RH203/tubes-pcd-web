from django import forms
from .models import CartoonImage

class CartoonImageForm(forms.ModelForm):
    class Meta:
        model = CartoonImage
        fields = ['title', 'image_upload']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Menyesuaikan untuk image_upload
        self.fields['image_upload'].widget = forms.ClearableFileInput(attrs={'multiple': True})
