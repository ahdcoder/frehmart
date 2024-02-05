from django import forms
from category.models import *
from subcategory.models import *
from .models import *

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),required=False)
    new_price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    old_price = forms.DecimalField(widget=forms.NumberInput(attrs=({'class':'form-control'})))
    image = forms.ImageField()

    class Meta:
        model = Product
        fields = ['name','subcategory','category','new_price','old_price','image']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','cols':45,'rows':6,'id':'comment_name'}))

    class Meta:
        model = Comment
        fields = ['comment']