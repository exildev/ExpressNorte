# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0009_time_despachado'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteWs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('identificacion', models.CharField(unique=True, max_length=15, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'identificacion no valida', b'invalid')])),
                ('telefono_fijo', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'telefono no valido', b'invalid')])),
                ('telefono_celular', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'telefono no valido', b'invalid')])),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoWS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_pedido', models.CharField(max_length=50)),
                ('npedido_express', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='TimeWS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creado', models.DateTimeField()),
                ('confirmado', models.DateTimeField(null=True)),
                ('alistado', models.DateTimeField(null=True)),
                ('despachado', models.DateTimeField(null=True)),
                ('entregado', models.DateTimeField(null=True)),
                ('pedido', models.OneToOneField(to='domicilios.PedidoWS')),
            ],
        ),
    ]
