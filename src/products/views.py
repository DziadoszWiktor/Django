#from urllib import request
from django.shortcuts import render
from .forms import ProductForm, RawProductForm
from .models import Product

# + : auto requirement field validation, many security features
# -: We can't use money filed (replaced with decimal field)
def product_create_view(request):
    form = RawProductForm()
    if request == "POST":
        form = RawProductForm(request.POST or None)
    context = {
        "form" : form
    }
    return render(request, "./products/product_create.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         "form":form
#     }
#     return render(request, "./products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "./products/product_detail.html", context)
