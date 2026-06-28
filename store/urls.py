from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.product_list, name='product_list'),
    path('productos/<slug:slug>/', views.product_detail, name='product_detail'),
    path('servicios/', views.service_list, name='service_list'),
]
