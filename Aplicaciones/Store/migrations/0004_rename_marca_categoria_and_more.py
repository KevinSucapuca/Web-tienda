# Generated by Django 4.1.7 on 2023-04-05 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_producto_descripcion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marca',
            new_name='Categoria',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Precio',
            new_name='PrecioActual',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='marca',
            new_name='categoria',
        ),
        migrations.AddField(
            model_name='producto',
            name='PrecioAnterior',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
    ]
