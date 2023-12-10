from django import forms

class CartoonImageForm(forms.Form):
    file_cartoon = forms.ImageField()
