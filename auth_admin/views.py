from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import *
from django.contrib.auth import authenticate,login,logout


def auth_login(request):
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/adminpanel/')
            
    form = LoginForm()
    context = {
        'form':form
    }
    return render(request,'adminpanel/auth_admin/login.html',context)

def auth_logout(request):
    logout(request)
    return redirect('/adminpanel/auth_login/')

def worker_all(request):
    if request.user.is_superuser:
        all_workers = User.objects.filter(is_superuser=True) and User.objects.filter(is_staff=True)

        context = {
            'all_workers':all_workers
        }
        return render(request,'adminpanel/auth_admin/worker_all.html',context)
    else:
        return redirect('/adminpanel/')

def worker_add(request):
    if request.method == 'POST':
        form = WorkerCreate(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            if user.is_superuser:
                user.is_superuser = True
                user.is_staff = True
                user.save()
            else:
                user.is_staff = True
                user.save()
            return redirect('/adminpanel/')     
    else:
        form = WorkerCreate()
    context = {
        'form':form
    }
    return render(request,'adminpanel/auth_admin/worker_add.html',context)




def worker_delete(request):
    if request.method == 'POST':
        worker_id = request.POST.get('worker_id')
        worker = User.objects.get(id=worker_id)
        worker.delete()
        return JsonResponse({},status=200)
    else:
        return JsonResponse({},status=200)
    
def change_password(request,i):
    user = User.objects.get(id=i)
    if request.method == 'POST':
        new_pass = request.POST.get('passowrd_1')
        user.set_password(new_pass)
        user.save()
        return redirect('/adminpanel/auth_admin/worker_all/')
    return render(request,'adminpanel/auth_admin/change_password.html',{'user':user})
    

# Create your views here.
