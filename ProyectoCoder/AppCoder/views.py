from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render
from .forms import *

def saludo(req):
 return HttpResponse("Hola coder")

def probando(req):
 mi_html = open('C:/Users/belu9/Desktop/EntregaPython/ProyectoCoder/AppCoder/static/index.html')
 plantilla = Template(mi_html.read())
 mi_html.close()
 contexto = Context()
 documento = plantilla.render(contexto)
 return HttpResponse(documento)

def inicio(request):
    return render(request, 'index.html')

def Contacto(request):
    return render(request, 'contacto.html')

def Sucursales(request):
    return render(request, 'sucursales.html')

def Pedidos(request):
    return render(request, 'pedidos.html')

def Productos(request):
    return render(request, 'productos.html')


def add_form(request):
    if request.method == "ADD":
        addproduct = AddProduct(request.ADD)

        if addproduct .is_valid():
            data = addproduct.cleaned_data
            newProd = Add(title=data['title'],
                            id=data['id'],
                            price=data['price'],
                            img=data['img'],
                            stock=data['stock']
                            )

            newProd.save()
            return redirect('index')

    addproduct = AddProduct()
    return render(request, 'productos.html', {'add_form': addproduct})


def order_form(request):
    if request.method == "ADD":
        addorder = AddOrder(request.ADD)

        if addorder.is_valid():
            data = addorder.cleaned_data
            newOrder = Order(number=data['number'],
                            address=data['address'],
                            products=data['products'],
                            user=data['user'])

            newOrder.save()
            return redirect('index')

    addorder = AddOrder()
    return render(request, 'pedidos.html', {'order_form': addorder})


def store_form(request):
    if request.method == "ADD":
        addstore = AddStores(request.ADD)

        if myStore.is_valid():
            data = myStore.cleaned_data
            newStore = Comment(username=data['username'],
                                  comment=data['comment'])

            newStore.save()
            return redirect('index')

    myStore = AddStores()
    return render(request, 'sucursales.html', {'comment_form': myStore})