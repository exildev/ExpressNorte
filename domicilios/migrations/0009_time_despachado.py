# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0008_auto_20160422_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='despachado',
            field=models.DateTimeField(null=True),
        ),
    ]
