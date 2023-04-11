# Generated by Django 4.1.7 on 2023-04-08 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_alter_producto_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Store.tag'),
            preserve_default=False,
        ),
    ]