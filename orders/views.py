from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from .models import Order, OrderItem
from .cart import Cart

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    return redirect('orders:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('orders:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'orders/cart_detail.html', {'cart': cart})

def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            postal_code=request.POST.get('postal_code'),
            city=request.POST.get('city'),
            phone=request.POST.get('phone')
        )
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        
        # In a real scenario we would redirect to a payment gateway here.
        # As per the requirement to include online payments (simulation), we set it as paid for demonstration
        # or we could show a payment form.
        order.paid = True 
        order.status = 'preparacion'
        order.save()
        
        return render(request, 'orders/created.html', {'order': order})
    return render(request, 'orders/checkout.html', {'cart': cart})
