# Generated by Django 4.1.7 on 2023-04-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0011_producto_descripcion2_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Estado',
            field=models.CharField(max_length=35, null=True),
        ),
    ]
