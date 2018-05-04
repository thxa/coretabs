from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category
# Create your views here.


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products,
               'categories': categories}

    return render(request, 'shop/product/list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product/detail.html', {'product': product})


def product_list_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'shop/product/category_by_product.html', {'category': category})
