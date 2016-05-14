# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0010_clientews_pedidows_timews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inicio', models.FloatField()),
                ('fin', models.FloatField()),
                ('puntos', models.ManyToManyField(to='mapa.Punto')),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pedido', models.ForeignKey(to='domicilios.PedidoWS')),
                ('ruta', models.OneToOneField(to='mapa.Ruta')),
            ],
        ),
    ]
