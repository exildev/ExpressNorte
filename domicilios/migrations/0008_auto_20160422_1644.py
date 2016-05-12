# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0007_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='tiempo_asignacion',
            new_name='alistado',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='tiempo_entrego',
            new_name='confirmado',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='tiempo_pedido',
            new_name='creado',
        ),
        migrations.AddField(
            model_name='time',
            name='entregado',
            field=models.DateTimeField(null=True),
        ),
    ]
