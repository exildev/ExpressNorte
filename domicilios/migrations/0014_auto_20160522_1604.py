# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0013_auto_20160521_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidows',
            name='npedido_express',
            field=models.CharField(max_length=50),
        ),
    ]
