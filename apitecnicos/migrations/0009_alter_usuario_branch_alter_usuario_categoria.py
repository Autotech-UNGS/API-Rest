# Generated by Django 4.2 on 2023-05-08 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitecnicos', '0008_alter_sucursal_id_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='branch',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='categoria',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
