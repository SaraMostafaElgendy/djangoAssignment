from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, User
from django.forms import modelform_factory

# Create your views here.
def detail(request,id):
    product=Product.objects.get(pk=id)
    return  render(request,"products/detail.html",{"product":product})

def all(request):
    return  render( request,"products/all.html",{"products": Product.objects.all()})


UserForm=modelform_factory(User,exclude=[])
def modelForm(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserForm();
    return  render(request, "products/modelForm.html", {'form': form})