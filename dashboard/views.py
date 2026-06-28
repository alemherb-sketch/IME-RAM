from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from store.models import Product, Category
from orders.models import Order
from django.db.models import Sum

def is_staff(user):
    return user.is_staff

def dashboard_login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard:home')
        else:
            messages.error(request, 'Credenciales inválidas o no tienes permisos de administrador.')
    return render(request, 'dashboard/login.html')

def dashboard_logout(request):
    logout(request)
    return redirect('dashboard:login')

@login_required(login_url='dashboard:login')
@user_passes_test(is_staff, login_url='dashboard:login')
def home(request):
    pending_orders = Order.objects.filter(status='pendiente').count()
    total_products = Product.objects.count()
    low_stock = Product.objects.filter(stock__lt=5).count()
    
    return render(request, 'dashboard/home.html', {
        'pending_orders': pending_orders,
        'total_products': total_products,
        'low_stock': low_stock
    })

@login_required(login_url='dashboard:login')
@user_passes_test(is_staff, login_url='dashboard:login')
def order_list(request):
    orders = Order.objects.all().order_by('-created')
    return render(request, 'dashboard/order_list.html', {'orders': orders})

@login_required(login_url='dashboard:login')
@user_passes_test(is_staff, login_url='dashboard:login')
def order_status_update(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, f'Estado del pedido #{order.id} actualizado a {order.get_status_display()}.')
    return redirect('dashboard:order_list')

@login_required(login_url='dashboard:login')
@user_passes_test(is_staff, login_url='dashboard:login')
def product_list(request):
    products = Product.objects.all().order_by('-created')
    return render(request, 'dashboard/product_list.html', {'products': products})

@login_required(login_url='dashboard:login')
@user_passes_test(is_staff, login_url='dashboard:login')
def product_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        cat_id = request.POST.get('category')
        category = get_object_or_404(Category, id=cat_id)
        Product.objects.create(
            category=category,
            name=request.POST.get('name'),
            slug=request.POST.get('name').lower().replace(' ', '-'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            stock=request.POST.get('stock'),
            available=request.POST.get('available') == 'on',
            image=request.FILES.get('image')
        )
        messages.success(request, 'Producto creado exitosamente.')
        return redirect('dashboard:product_list')
    return render(request, 'dashboard/product_form.html', {'categories': categories})

@login_required(login_url='dashboard:login')
@user_passes_test(is_staff, login_url='dashboard:login')
def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        cat_id = request.POST.get('category')
        product.category = get_object_or_404(Category, id=cat_id)
        product.name = request.POST.get('name')
        product.slug = request.POST.get('name').lower().replace(' ', '-')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.available = request.POST.get('available') == 'on'
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        product.save()
        messages.success(request, 'Producto actualizado exitosamente.')
        return redirect('dashboard:product_list')
    return render(request, 'dashboard/product_form.html', {'product': product, 'categories': categories})

@login_required(login_url='dashboard:login')
@user_passes_test(is_staff, login_url='dashboard:login')
def banner_edit(request):
    from store.models import Banner
    banners = Banner.objects.all().order_by('-created')
    if request.method == 'POST':
        if request.FILES.get('image'):
            Banner.objects.create(image=request.FILES.get('image'), active=True)
            messages.success(request, 'Banner agregado exitosamente.')
        return redirect('dashboard:banner_edit')
    return render(request, 'dashboard/banner_form.html', {'banners': banners})

@login_required(login_url='dashboard:login')
@user_passes_test(is_staff, login_url='dashboard:login')
def banner_delete(request, banner_id):
    from store.models import Banner
    banner = get_object_or_404(Banner, id=banner_id)
    banner.delete()
    messages.success(request, 'Banner eliminado exitosamente.')
    return redirect('dashboard:banner_edit')
