from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout

def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,"adminpanel/index.html")
    else:
        return redirect('/adminpanel/auth_login/')



# Create your views here.
