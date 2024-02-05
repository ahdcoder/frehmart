from django.shortcuts import render,redirect
from .models import Product
from .forms import *
from django.http import JsonResponse

def all(request):
    all_products = Product.objects.all()
    context = {
        'all_products':all_products,
    }
    return render(request,'adminpanel/product/all.html',context)

def add(request):
    form = ProductForm
    if request.method == 'POST':
        ProductForm(request.POST,request.FILES).save()
        return redirect('/adminpanel/product/all/')
    context = {
        'form':form
    }
    return render(request,'adminpanel/product/add.html',context)

def edit(request,i):
    select_product = Product.objects.get(id=i)
    form = ProductForm(instance=select_product)
    if request.method == 'POST':
        ProductForm(request.POST,request.FILES,instance=select_product).save()
        return redirect('/adminpanel/product/all/')
    context = {
        'form':form,
        'select_form':select_product
    }
    return render(request,'adminpanel/product/edit.html',context)

def delete(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        product.delete()

        return JsonResponse({},status=200)
    else:
        return JsonResponse({},status=400)
    

def detail(request,i):
    select_product = Product.objects.get(id=i)
    return render(request,'adminpanel/product/detail.html',{'s_pro':select_product})

    

# Create your views here.
