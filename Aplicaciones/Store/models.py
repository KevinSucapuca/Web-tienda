from django.db import models

class Categoria (models.Model):
    Nombre = models.CharField(max_length=35)
    def __str__(self):
        texto = "{0}"
        return texto.format(self.Nombre)

class Producto(models.Model):
    NombreProducto=models.CharField(max_length=35)
    PrecioActual=models.DecimalField(max_digits=6, decimal_places=2)
    PrecioAnterior=models.DecimalField(max_digits=6, decimal_places=2)
    Estado=models.CharField(max_length=35)
    foto=models.URLField(max_length = 300)
    Descripcion=models.CharField(max_length=250)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
    def __str__(self):
        texto = "{0} {1} {2} {3} {4}"
        return texto.format(self.NombreProducto, self.PrecioActual,self.PrecioAnterior, self.Estado, self.foto, self.categoria)

