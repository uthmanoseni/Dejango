# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, CatalogueForm
from .models import Product, Catalogue
from django.contrib import messages

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {'message': 'welcome to my Django homepage!'})

def form_view(request):
    return render(request, 'form.html', {'message': 'Feel free your Data is safe with me!'})


# ====== PRODUCT CRUD ======
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully!")
            return redirect('product_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('product_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'object': product})





# ====== CATALOGUE CRUD ======
def catalogue_list(request):
    catalogues = Catalogue.objects.all()
    return render(request, 'catalogue_list.html', {'catalogues': catalogues})


def catalogue_create(request):
    if request.method == 'POST':
        form = CatalogueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Catalogue created successfully!")
            return redirect('catalogue_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CatalogueForm()
    return render(request, 'catalogue_form.html', {'form': form})


def catalogue_update(request, pk):
    catalogue = get_object_or_404(Catalogue, pk=pk)
    if request.method == 'POST':
        form = CatalogueForm(request.POST, instance=catalogue)
        if form.is_valid():
            form.save()
            messages.success(request, "Catalogue updated successfully!")
            return redirect('catalogue_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CatalogueForm(instance=catalogue)
    return render(request, 'catalogue_form.html', {'form': form})


def catalogue_delete(request, pk):
    catalogue = get_object_or_404(Catalogue, pk=pk)
    if request.method == 'POST':
        catalogue.delete()
        messages.success(request, "Catalogue deleted successfully!")
        return redirect('catalogue_list')
    return render(request, 'catalogue_confirm_delete.html', {'object': catalogue})