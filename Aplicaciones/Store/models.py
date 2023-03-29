from django.db import models

class Marca (models.Model):
    Nombre = models.CharField(max_length=35)
    def __str__(self):
        texto = "{0}"
        return texto.format(self.Nombre)

class Producto(models.Model):
    NombreProducto=models.CharField(max_length=35)
    Precio=models.DecimalField(max_digits=6, decimal_places=2)
    Estado=models.CharField(max_length=35)
    foto=models.URLField(max_length = 300)
    Marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    
    def __str__(self):
        texto = "{0} {1} {2} {3} {4}"
        return texto.format(self.NombreProducto, self.Precio, self.Estado, self.foto, self.marca)

