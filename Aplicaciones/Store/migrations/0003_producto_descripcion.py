# Generated by Django 4.1.7 on 2023-03-29 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_rename_marca_producto_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Descripcion',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]