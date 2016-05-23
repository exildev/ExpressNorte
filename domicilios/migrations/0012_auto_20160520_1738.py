# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0011_auto_20160514_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidows',
            name='items',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pedidows',
            name='cliente',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
