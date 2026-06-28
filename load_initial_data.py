import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from store.models import Product

if Product.objects.count() == 0:
    print("La base de datos está vacía. Cargando datos iniciales...")
    call_command('loaddata', 'data.json')
else:
    print("La base de datos ya contiene productos. Saltando la carga inicial.")
