from django.db import models
from django.utils.text import slugify

class Categoria (models.Model):
    Nombre = models.CharField(max_length=35)
    def __str__(self):
        texto = "{0}"
        return texto.format(self.Nombre)
    
class Tag (models.Model):
    Nombre = models.CharField(max_length=35)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        slug = slugify(self.Nombre)
        slug_exists = Tag.objects.filter(categoria=self.categoria, slug=slug).exists()
        if slug_exists:
            slug = f"{slugify(self.categoria.Nombre)}-{slug}"
        self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.Nombre, self.categoria)

class Producto(models.Model):
    NombreProducto=models.CharField(max_length=70)
    PrecioActual=models.DecimalField(max_digits=6, decimal_places=2)
    PrecioAnterior=models.DecimalField(max_digits=6, decimal_places=2)
    Estado=models.CharField(max_length=35,  null=True)
    foto=models.URLField(max_length = 300)
    Descripcion=models.CharField(max_length=500)
    Descripcion2=models.CharField(max_length=500)
    tag=models.ForeignKey(Tag, on_delete=models.PROTECT)
    
    
    def __str__(self):
        texto = "{0} {1} {2} {3} {4}"
        return texto.format(self.NombreProducto, self.PrecioActual,self.PrecioAnterior, self.Estado, self.foto,self.Descripcion,self.tag)

