from django import forms
from category.models import *
from .models import Subcategory

class SubcategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    icon = forms.ImageField()

    class Meta:
        model = Subcategory
        fields = ['name','category','icon']