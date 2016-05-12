# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0005_auto_20160421_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='alistado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pedido',
            name='confirmado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pedido',
            name='despachado',
            field=models.BooleanField(default=False),
        ),
    ]
