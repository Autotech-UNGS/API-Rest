from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id_empleado','nombre_completo','dni','nombre_usuario','categoria','contrasena',
        'tipo','branch','id_contacto','id_direccion','categoria')
        read_only_fields = ('id_empleado','nombre_completo','dni','nombre_usuario','categoria','contrasena',
        'tipo','branch','id_contacto','id_direccion','categoria',)


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id_sucursal','nombre','id_direccion','telefono')
        read_only_fields = ('id_sucursal','nombre','id_direccion','telefono')

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('id_direccion','calle','ciudad','estado','codigo_postal','pais','altura')
        read_only_fields = ('id_direccion','calle','ciudad','estado','codigo_postal','pais','altura')

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ('id_contacto','email','codigo_telefono','numero_telefono')
        read_only_fields = ('id_contacto','email','codigo_telefono','numero_telefono')