from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.dashboard_login, name='login'),
    path('logout/', views.dashboard_logout, name='logout'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/status/', views.order_status_update, name='order_status_update'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_create'),
    path('products/<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('banner/', views.banner_edit, name='banner_edit'),
    path('banner/<int:banner_id>/delete/', views.banner_delete, name='banner_delete'),
]
