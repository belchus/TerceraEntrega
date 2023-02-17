"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder.views import *
from AppCoder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('busqueda/', Resultados),
    path('sucursales/', Sucursales),
    path('pedidos/', Pedidos),
    path('productos/', Productos),
    path('add_form/', add_form, name='add_form'),
    path('order_form/', order_form, name='order_form'),
    path('store_form/', store_form, name='store_form'),
    path('find_product/', add_form, name='find_product'),
]
