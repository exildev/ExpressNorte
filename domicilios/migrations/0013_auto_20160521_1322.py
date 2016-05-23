# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0012_auto_20160520_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidows',
            name='tipo_pago',
            field=models.CharField(max_length=50),
        ),
    ]
