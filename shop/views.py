from django.shortcuts import render
from shop.models import Category, Product

# @login_required
def shop(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'shop.html', context)

def product_details(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'product-details.html', context)

def cart(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'cart.html', context)