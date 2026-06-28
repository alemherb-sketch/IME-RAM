import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

c = Client(HTTP_HOST='127.0.0.1')
u = User.objects.get(username='admin') if User.objects.filter(username='admin').exists() else User.objects.first()
c.force_login(u)

response = c.get('/panel/')
html = response.content.decode('utf-8')

match = re.search(r'<nav class="sidebar-nav">(.*?)</nav>', html, re.DOTALL)
if match:
    print(match.group(1))
else:
    print("NOT FOUND")
