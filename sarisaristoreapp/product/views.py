from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreate
from django.http import HttpResponse

# Create your views here.
# READ
def index(request):
    shelf = Product.objects.all()
    return render(request, 'product/prod-library.html', {'shelf':shelf})

# CREATE
def upload(request):
    upload = ProductCreate()
    if request.method == "POST":
        upload = ProductCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload""")
    else:
        return render(request, 'product/upload_form.html', {'upload_form': upload})
    
# UPDATE
def update_product(request, prod_id):
    prod_id = int(prod_id)
    try:
        prod_sel = Product.objects.get(id = prod_id)
    except Product.DoesNotExist:
        return redirect('index')
    prod_form = ProductCreate(request.POST or None, instance=prod_sel)

    if prod_form.is_valid():
        prod_form.save()
        return redirect('index')
    return render(request, 'product/upload_form.html', {'upload_form': prod_form})

# Delete
def delete_product(request, prod_id):
    prod_id = int(prod_id)
    try:
        prod_sel = Product.objects.get(id = prod_id)
    except Product.DoesNotExist:
        return redirect('index')
    prod_sel.delete()
    return redirect('index')




