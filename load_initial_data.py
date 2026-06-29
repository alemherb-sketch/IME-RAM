import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from store.models import Product
from django.contrib.auth.models import User

if Product.objects.count() == 0:
    print("La base de datos está vacía. Cargando datos iniciales...")
    call_command('loaddata', 'data.json')
else:
    print("La base de datos ya contiene productos. Saltando la carga inicial.")

# Ensure admin user exists and reset password
admin_user, created = User.objects.get_or_create(username='admin', defaults={
    'email': 'admin@imeram.com',
    'is_superuser': True,
    'is_staff': True
})
admin_user.set_password('admin123')
admin_user.is_superuser = True
admin_user.is_staff = True
admin_user.save()
print("Cuenta de administrador ('admin') configurada con la contraseña: 'admin123'")
