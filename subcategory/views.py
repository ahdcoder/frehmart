from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import SubcategoryForm
from .models import *
from django.http import JsonResponse

def all(request):
    form = SubcategoryForm
    select_sub = Subcategory.objects.all()


    context = {
        'form':form,
        'select_sub':select_sub,
    }

    return render(request,'adminpanel/subcategory/all.html',context)

def save(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST,request.FILES)
        if form.is_valid():
            sub = form.save(commit=False)
            category = sub.category
            category.status = 2
            category.save()
            sub.save() 
            return redirect('/adminpanel/subcategory/all/')


    
def delete(request):
    if request.method == 'POST':
        subcategory_id = request.POST.get('subcategory_id')
        subcategory = Subcategory.objects.get(id=subcategory_id)
        subcategory.delete()

        return JsonResponse({},status=200)
    else:
        return JsonResponse({},status=400)
    
def edit(request,i):
    subcategory = Subcategory.objects.get(id=i)
    form = SubcategoryForm(instance=subcategory)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST,request.FILES,instance=subcategory).save()
        return redirect('/adminpanel/subcategory/all/')

    context = {
        'form':form,
        'subcategory':subcategory
    }
    return render(request,'adminpanel/subcategory/edit.html',context)
    


    
    


# Create your views here.
