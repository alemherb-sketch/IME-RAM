from django.db import models
from store.models import Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('preparacion', 'En Preparación'),
        ('camino', 'En Camino'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    )
    
    first_name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellidos")
    email = models.EmailField(verbose_name="Correo Electrónico")
    address = models.CharField(max_length=250, verbose_name="Dirección de Entrega")
    postal_code = models.CharField(max_length=20, verbose_name="Código Postal", blank=True)
    city = models.CharField(max_length=100, verbose_name="Ciudad")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    paid = models.BooleanField(default=False, verbose_name="Pagado")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente', verbose_name="Estado de Entrega")

    class Meta:
        ordering = ['-created']
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f'Pedido {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Cantidad")

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
