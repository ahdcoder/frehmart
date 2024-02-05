from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))

    class Meta:
        model = Category
        fields = ['name']