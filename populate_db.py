import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from store.models import Category, Product

# Categories
cat_cables, _ = Category.objects.get_or_create(name='Cables Eléctricos', slug='cables-electricos', description='Cables para instalaciones domiciliarias e industriales.')
cat_iluminacion, _ = Category.objects.get_or_create(name='Iluminación', slug='iluminacion', description='Focos, luminarias y reflectores LED.')
cat_interruptores, _ = Category.objects.get_or_create(name='Interruptores y Tomacorrientes', slug='interruptores-tomacorrientes', description='Placas, interruptores y tomacorrientes de pared.')
cat_tableros, _ = Category.objects.get_or_create(name='Tableros y Llaves', slug='tableros-llaves', description='Tableros eléctricos y llaves termomagnéticas.')
cat_tubos, _ = Category.objects.get_or_create(name='Tubos y Canaletas', slug='tubos-canaletas', description='Tuberías PVC y canaletas para cableado.')

products = [
    {
        'category': cat_cables,
        'name': 'Cable THW 14 AWG x 100m - Indeco',
        'slug': 'cable-thw-14-awg-100m-indeco',
        'description': 'Rollo de cable rígido THW calibre 14 AWG de marca Indeco (Perú). Ideal para instalaciones eléctricas fijas interiores.',
        'price': 145.50,
        'stock': 50
    },
    {
        'category': cat_cables,
        'name': 'Cable Mellizo 2x16 AWG x 100m - Indeco',
        'slug': 'cable-mellizo-2x16-awg-100m-indeco',
        'description': 'Cable flexible mellizo ideal para extensiones cortas y aparatos portátiles livianos.',
        'price': 85.00,
        'stock': 30
    },
    {
        'category': cat_iluminacion,
        'name': 'Foco LED 12W Luz Blanca - Philips',
        'slug': 'foco-led-12w-luz-blanca-philips',
        'description': 'Foco LED E27 de 12W (equivale a 100W incandescente) luz fría para alta iluminación.',
        'price': 12.00,
        'stock': 100
    },
    {
        'category': cat_iluminacion,
        'name': 'Reflector LED 50W Exterior - Opalux',
        'slug': 'reflector-led-50w-exterior-opalux',
        'description': 'Reflector LED de alta potencia para exteriores, protección IP65.',
        'price': 45.00,
        'stock': 20
    },
    {
        'category': cat_interruptores,
        'name': 'Interruptor Simple Modus Style - Bticino',
        'slug': 'interruptor-simple-modus-style-bticino',
        'description': 'Placa armada de 1 interruptor simple de la línea Modus Style, color blanco.',
        'price': 14.50,
        'stock': 60
    },
    {
        'category': cat_interruptores,
        'name': 'Tomacorriente Doble Universal - Bticino',
        'slug': 'tomacorriente-doble-universal-bticino',
        'description': 'Tomacorriente doble universal con toma a tierra, línea Modus Plus.',
        'price': 18.00,
        'stock': 75
    },
    {
        'category': cat_tableros,
        'name': 'Llave Termomagnética 2x20A - ABB',
        'slug': 'llave-termomagnetica-2x20a-abb',
        'description': 'Interruptor termomagnético bipolar de 20 amperios, riel DIN.',
        'price': 25.00,
        'stock': 40
    },
    {
        'category': cat_tableros,
        'name': 'Interruptor Diferencial 2x40A - Schneider',
        'slug': 'interruptor-diferencial-2x40a-schneider',
        'description': 'Salvavidas diferencial de 30mA para protección contra descargas eléctricas.',
        'price': 110.00,
        'stock': 15
    },
    {
        'category': cat_tableros,
        'name': 'Tablero Eléctrico de Empotrar 12 Polos - Ticino',
        'slug': 'tablero-electrico-empotrar-12-polos-ticino',
        'description': 'Tablero de distribución para empotrar, capacidad de 12 polos, tapa transparente.',
        'price': 55.00,
        'stock': 10
    },
    {
        'category': cat_tubos,
        'name': 'Tubo PVC SEL 3/4" x 3m - Pavco',
        'slug': 'tubo-pvc-sel-3-4-x-3m-pavco',
        'description': 'Tubo PVC eléctrico clase SEL de 3/4 de pulgada de diámetro y 3 metros de largo.',
        'price': 4.50,
        'stock': 200
    }
]

for p in products:
    Product.objects.update_or_create(
        slug=p['slug'],
        defaults=p
    )

print("¡10 Productos peruanos de ejemplo insertados correctamente en la base de datos!")
