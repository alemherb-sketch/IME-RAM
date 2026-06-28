import os
import django
import traceback

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

c = Client(HTTP_HOST='127.0.0.1')
u = User.objects.get(username='admin') if User.objects.filter(username='admin').exists() else User.objects.first()
c.force_login(u)

try:
    response = c.get('/panel/')
    print("SUCCESS", response.status_code)
except Exception as e:
    traceback.print_exc()
