# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0014_auto_20160522_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=500)),
                ('fijo', models.CharField(max_length=10, verbose_name=b'Telefono Fijo')),
                ('celular', models.CharField(max_length=10, verbose_name=b'Telefono Celular')),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('empresa', models.ForeignKey(to='domicilios.Empresa')),
            ],
        ),
    ]
