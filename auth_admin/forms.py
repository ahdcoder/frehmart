from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form__input','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form__input','placeholder':'Password'}))


class WorkerCreate(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','name':'username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','name':'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','name':'last_name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','name':'password1'}),required=False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','name':'paswword2'}),required=False)
    is_superuser = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username','password1','password2','first_name','last_name','is_superuser']
