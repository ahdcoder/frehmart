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
    all_workers = User.objects.filter(is_superuser=True) or User.objects.filter(is_staff=True)

    context = {
        'all_workers':all_workers
    }
    return render(request,'adminpanel/auth_admin/worker_all.html',context)

def worker_add(request):
    if request.method == 'POST':
        form = WorkerCreate(request.POST)
        print('fsdfdsfdsf')
        if form.is_valid():
            form.save()
            return redirect('/adminpanel/')
            



    else:
        form = WorkerCreate()
    context = {
        'form':form
    }
    return render(request,'adminpanel/auth_admin/worker_add.html',context)

def worker_edit(request,i):
    form = User.objects.get(id=i)
    if request.method == 'POST':
        worker_form_2 = WorkerCreate(request.POST,instance = form)
        if worker_form_2.is_valid():
            worker_form_2.save()
            return redirect('/adminpanel/auth_admin/worker_all/')
    worker_form = WorkerCreate(instance=form)

    context = {
        'form':worker_form
    }
    return render(request,'adminpanel/auth_admin/worker_edit.html',context)

def worker_delete(request):
    if request.method == 'POST':
        worker_id = request.POST.get('worker_id')
        worker = User.objects.get(id=worker_id)
        worker.delete()
        return JsonResponse({},status=200)
    else:
        return JsonResponse({},status=200)
        
    

# Create your views here.
