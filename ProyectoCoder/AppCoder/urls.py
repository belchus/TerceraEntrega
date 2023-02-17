from django.urls import include, path
from AppCoder import views


urlpatterns = [
    path('', views.inicio),
    path('busqueda/',views.Busqueda),
    path('sucursales/', views.Sucursales),
    path('pedidos/', views.Pedidos),
    path('productos/', views.Productos),
    path('add_form/', views.add_form, name='add_form'),
    path('order_form/', views.order_form, name='order_form'),
    path('store_form/', views.store_form, name='store_form'),
    path('find_product/', views.find_product, name='find_product'),
    path('resultados/',views.Resultados,name='resultados'),
]
