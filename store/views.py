from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Service, Banner

def index(request):
    featured_products = Product.objects.filter(available=True)[:6]
    services = Service.objects.filter(active=True)[:3]
    banners = Banner.objects.filter(active=True)
    return render(request, 'store/index.html', {
        'featured_products': featured_products,
        'services': services,
        'banners': banners
    })

def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})

def service_list(request):
    services = Service.objects.filter(active=True)
    return render(request, 'store/service_list.html', {'services': services})
