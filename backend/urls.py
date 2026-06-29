from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve as media_serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel/', include('dashboard.urls', namespace='dashboard')),
    path('pedidos/', include('orders.urls', namespace='orders')),
    path('', include('store.urls', namespace='store')),
]

# Personalización del Panel de Administración
admin.site.site_header = 'Administración de IME RAM'
admin.site.site_title = 'Panel de IME RAM'
admin.site.index_title = 'Gestión de la Tienda Virtual'

# Servir archivos de media subidos en runtime (ej. banners del panel).
# WhiteNoise solo sirve lo que existía al hacer collectstatic en el build
# (STATIC_ROOT); para los archivos subidos por el admin, que se guardan en
# MEDIA_ROOT, agregamos este patrón que funciona también con DEBUG=False.
# (Para paths ya recogidos en el build, WhiteNoise responde antes que esto.)
_media_prefix = settings.MEDIA_URL.lstrip('/')
urlpatterns += [
    re_path(r'^%s(?P<path>.*)$' % _media_prefix, media_serve,
            {'document_root': settings.MEDIA_ROOT}),
]
