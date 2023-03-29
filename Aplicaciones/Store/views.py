from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Producto
from django.core.paginator import Paginator
from .models import Producto
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




def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    context = {'producto': producto}
    return render(request, 'detalle_producto.html', context)