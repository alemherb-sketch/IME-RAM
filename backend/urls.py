from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel/', include('dashboard.urls', namespace='dashboard')),
    path('pedidos/', include('orders.urls', namespace='orders')),
    path('', include('store.urls', namespace='store')),
]

# Personalización del Panel de Administración
admin.site.site_header = 'Administración de GRUPO COINP'
admin.site.site_title = 'Panel de GRUPO COINP'
admin.site.index_title = 'Gestión de la Tienda Virtual'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
