from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Producto,Categoria,Tag
from django.core.paginator import Paginator
import re
# Create your views here.


def home(request):
    
    categorias = Categoria.objects.all()

    for categoria in categorias:
        categoria.tags = Tag.objects.filter(categoria=categoria)


    dataproducto = Producto.objects.all().order_by('-id')  
    paginator = Paginator(dataproducto, 9)
    pagina = request.GET.get('page') or 1
    dataproducto = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, dataproducto.paginator.num_pages + 1)
    
    if 'buscar' in request.GET:
        producto = request.GET['buscar']
        dataproducto = Producto.objects.filter(
            Q(NombreProducto__icontains=producto) |
            Q(Marca__icontains=producto))
        paginator = Paginator(dataproducto, 9)
        pagina = request.GET.get('page') or 1
        dataproducto = paginator.get_page(pagina)
        pagina_actual = int(pagina)
        paginas = range(1, dataproducto.paginator.num_pages + 1)

    context = {
        'dataproducto': dataproducto,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
        'categorias': categorias,
    }

    return render(request, 'galeria.html', context)

    # dataproducto = Producto.objects.all().order_by('-id')  
    # paginator = Paginator(dataproducto, 9)
    # pagina = request.GET.get('page') or 1
    # dataproducto = paginator.get_page(pagina)
    # pagina_actual = int(pagina)
    # paginas = range(1, dataproducto.paginator.num_pages + 1)
    
    # if 'buscar' in request.GET:
    #     producto = request.GET['buscar']
    #     dataproducto = Producto.objects.filter(
    #         Q(NombreProducto__icontains=producto) |
    #         Q(Marca__icontains=producto))
    #     paginator = Paginator(dataproducto, 9)
    #     pagina = request.GET.get('page') or 1
    #     dataproducto = paginator.get_page(pagina)
    #     pagina_actual = int(pagina)
    #     paginas = range(1, dataproducto.paginator.num_pages + 1)
    
    # return render(request, 'galeria.html', {'dataproducto': dataproducto, 'paginas': paginas, 'pagina_actual': pagina_actual})


def mi_vista(request):
    categorias = Categoria.objects.all()

    for categoria in categorias:
        categoria.tags = Tag.objects.filter(categoria=categoria)

    context = {
        'categorias': categorias
    }

    return render(request, 'galeria.html', context)


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    context = {'producto': producto}
    return render(request, 'detalle_producto.html', context)

def SearchProducto(request):
    
    dataproducto = []
    dataproducto = Producto.objects.all()
    if 'buscar' in request.GET:
        #producto = request.GET['buscar']
        #dataproducto = Producto.objects.filter(
            #Q(NombreProducto__icontains=producto))
        producto = request.GET['buscar']
        palabras = producto.split()

        # construir expresión regular para buscar todas las palabras en cualquier orden
        regex = '.*' + '.*'.join(palabras) + '.*'

        # buscar en el campo NombreProducto
        dataproducto = Producto.objects.filter(NombreProducto__iregex=regex)
        
    paginator = Paginator(dataproducto, 9)
    pagina = request.GET.get('page') or 1
    dataproducto = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, dataproducto.paginator.num_pages + 1)   
    categorias = Categoria.objects.all()

    for categoria in categorias:
        categoria.tags = Tag.objects.filter(categoria=categoria)
            
    context = {
        'dataproducto': dataproducto,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
        'categorias': categorias,
    }

    return render(request, 'galeria.html', context)


def SearchLiquidacion(request):
    
    productos = []
    productos = Producto.objects.all()
    if 'buscar' in request.GET:
        #producto = request.GET['buscar']
        #dataproducto = Producto.objects.filter(
            #Q(NombreProducto__icontains=producto))
        producto = request.GET['buscar']
        palabras = producto.split()

        # construir expresión regular para buscar todas las palabras en cualquier orden
        regex = '.*' + '.*'.join(palabras) + '.*'

        # buscar en el campo NombreProducto
        
        
        productos = Producto.objects.filter(
            Q(NombreProducto__iregex=regex) & Q(Estado__iexact='Liquidacion'))
    paginator = Paginator(productos, 9)
    pagina = request.GET.get('page') or 1
    productos = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, productos.paginator.num_pages + 1)
    
    categorias = Categoria.objects.all()

    for categoria in categorias:
        categoria.tags = Tag.objects.filter(categoria=categoria)
        
    context = {
        'productos': productos,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
        'categorias': categorias,
    }

    return render(request, 'liquidacion.html', context)


def Liquidacion(request):
    categorias = Categoria.objects.all()

    for categoria in categorias:
        categoria.tags = Tag.objects.filter(categoria=categoria)


    productos = Producto.objects.filter(Estado__icontains='Liquidacion')
    paginator = Paginator(productos, 9)
    pagina = request.GET.get('page') or 1
    productos = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, productos.paginator.num_pages + 1)
    
    return render(request, 'Liquidacion.html', {'productos': productos, 'paginas': paginas, 'pagina_actual': pagina_actual,'categorias': categorias})



def mostrar_productos_por_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    productos = Producto.objects.filter(tag=tag).distinct()
    
    categorias = Categoria.objects.all()
    for categoria in categorias:
        categoria.tags = Tag.objects.filter(categoria=categoria)
        
    
        
    dataproducto = Producto.objects.all()
    paginator = Paginator(dataproducto, 9)
    pagina = request.GET.get('page') or 1
    dataproducto = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, dataproducto.paginator.num_pages + 1)
    context = {
        
        'productos': productos,
        'tag': tag,
        'categorias': categorias,
        'dataproducto': dataproducto,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
    }
    return render(request, 'productos_por_tag.html', context)

def mostrar_productos_por_tag_liquidacion(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    productos = Producto.objects.filter(tag=tag, Estado='Liquidacion').distinct()
    
    categorias = Categoria.objects.all()
    for categoria in categorias:
        categoria.tags = Tag.objects.filter(categoria=categoria)
        
    dataproducto = Producto.objects.all()
    paginator = Paginator(dataproducto, 9)
    pagina = request.GET.get('page') or 1
    dataproducto = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, dataproducto.paginator.num_pages + 1)
    
    
    context = {
        
        'productos': productos,
        'tag': tag,
        'categorias': categorias,
        'dataproducto': dataproducto,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
    }
    return render(request, 'liquidacion.html', context)



def otros_productos(request):
    
    dataproducto = Producto.objects.filter(Estado__icontains='Otros')  
    paginator = Paginator(dataproducto, 9)
    pagina = request.GET.get('page') or 1
    dataproducto = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, dataproducto.paginator.num_pages + 1)

    context = {
        'dataproducto': dataproducto,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
        
    }

    return render(request, 'otros_productos.html', context)