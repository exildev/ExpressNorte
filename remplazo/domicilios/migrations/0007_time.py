# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0006_auto_20160422_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiempo_pedido', models.DateTimeField()),
                ('tiempo_asignacion', models.DateTimeField(null=True)),
                ('tiempo_entrego', models.DateTimeField(null=True)),
                ('pedido', models.OneToOneField(to='domicilios.Pedido')),
            ],
            options={
                'verbose_name': 'Time',
                'verbose_name_plural': 'Times',
            },
        ),
    ]
