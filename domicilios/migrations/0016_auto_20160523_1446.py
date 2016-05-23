# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0015_tienda'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='nit',
            field=models.CharField(default=1, unique=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tienda',
            name='celular',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Telefono Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='tienda',
            name='fijo',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Telefono Fijo', blank=True),
        ),
    ]
