from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="Categoría")
    name = models.CharField(max_length=200, verbose_name="Nombre")
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del Servicio")
    description = models.TextField(verbose_name="Descripción")
    base_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio Base (Opcional)")
    image = models.ImageField(upload_to='services/', blank=True, verbose_name="Imagen")
    active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/', verbose_name="Imagen")
    active = models.BooleanField(default=True, verbose_name="Activo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")

    class Meta:
        verbose_name = "Banner Principal"
        verbose_name_plural = "Banners Principales"

    def __str__(self):
        return f"Banner {self.id} - {'Activo' if self.active else 'Inactivo'}"
