from django.shortcuts import render
from django.db.models import Q
from .models import Producto
from django.core.paginator import Paginator
# Create your views here.


def home(request):

    dataproducto = Producto.objects.all().order_by('-id')
    paginator = Paginator(dataproducto, 8)
    pagina = request.GET.get('page') or 1
    dataproducto = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, dataproducto.paginator.num_pages + 1)
    
    if 'buscar' in request.GET:
        callsign = request.GET['buscar']
        dataproducto = Producto.objects.filter(
            Q(NombreProducto__icontains=callsign) |
            Q(Marca__icontains=callsign))
        paginator = Paginator(dataproducto, 8)
        pagina = request.GET.get('page') or 1
        dataproducto = paginator.get_page(pagina)
        pagina_actual = int(pagina)
        paginas = range(1, dataproducto.paginator.num_pages + 1)
    
    return render(request, 'galeria.html', {'dataproducto': dataproducto, 'paginas': paginas, 'pagina_actual': pagina_actual})
