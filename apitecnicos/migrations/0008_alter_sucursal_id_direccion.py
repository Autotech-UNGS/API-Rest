# Generated by Django 4.2 on 2023-05-08 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apitecnicos', '0007_alter_contacto_codigo_telefono_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='id_direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apitecnicos.direccion'),
        ),
    ]
