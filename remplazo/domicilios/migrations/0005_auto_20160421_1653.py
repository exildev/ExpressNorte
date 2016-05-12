# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0004_auto_20160407_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='entregado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cargo',
            field=models.CharField(max_length=20, choices=[(b'', b'Selccion un Cargo'), (b'ADMINISTRADOR', b'Administrador'), (b'SUPERVISOR', b'Supervisor'), (b'ALISTADOR', b'Alistador'), (b'MOTORIZADO', b'Motorizado')]),
        ),
    ]
