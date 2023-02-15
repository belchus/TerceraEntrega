from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render,redirect
from .forms import *
from .models import *

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

def Resultados(request):
    return render(request, 'busqueda.html')


def add_form(request):
    if request.method == "POST":
        addproduct = AddProduct(request.POST)

        if addproduct .is_valid():
            data = addproduct.cleaned_data
            newProd = Product(
                title=data['title'],
                code=data['title'],
                            
                price=data['price'],
                stock=data['stock']
                            )

            newProd.save()
            return redirect('index')


        else:
            return render(request, 'productos.html', {'addprosuct': add_form})
    
    addproduct = AddProduct()
    return render(request, 'productos.html', {'addproduct': AddProduct})


def order_form(request):
    if request.method == "POST":
        addorder = AddOrder(request.POST)

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
    if request.method == "POST":
        myStore = AddStores(request.POST)

        if myStore.is_valid():
            data = myStore.cleaned_data
            newStore = Stores(name=data['name'],
                             address=data['address'],
                             phone=data['phone'],
                              online=data['online'])

            newStore.save()
            return redirect('index')

    myStore = AddStores()
    return render(request, 'sucursales.html', {'store_form': myStore})


def find_product(req):

    if req.GET['title']:
        isProd = req.GET['title']
        title = title.objects.filter(title__icontains=isProd)

        return render(req, 'busqueda.html', {'title': isProd})

    else:
        respuesta = "El producto no existe"

    return HttpResponse(respuesta)

    
def find_order(req):

    if req.GET['number']:
        isOrder = req.GET['number']
        number = number.objects.filter(number__icontains=isOrder)

        return render(req, 'busqueda.html', {'title': isOrder})

    else:
        respuesta = "El numero de orden buscada no existe"

    return HttpResponse(respuesta)