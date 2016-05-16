# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0010_clientews_pedidows_timews'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidows',
            name='alistado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='alistador',
            field=models.ForeignKey(related_name='alistadorws', to='domicilios.Empleado', null=True),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='cliente',
            field=models.ForeignKey(to='domicilios.ClienteWs', null=True),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='confirmado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='despachado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='empresa',
            field=models.ForeignKey(blank=True, to='domicilios.Empresa', null=True),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='entregado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='fecha_pedido',
            field=models.DateField( auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidows',
            name='motorizado',
            field=models.ForeignKey(related_name='motorizado_enviadows', to='domicilios.Empleado', null=True),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='observacion',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='supervisor',
            field=models.ForeignKey(related_name='supervisorws', to='domicilios.Empleado', null=True),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='tienda',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='tipo_pago',
            field=models.CharField(default=b'EFECTIVO', max_length=50, choices=[(b'EFECTIVO', b'Efectivo'), (b'TARJETA', b'Tarjeta'), (b'REMISION', b'Remision')]),
        ),
        migrations.AddField(
            model_name='pedidows',
            name='total',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2),
        ),
    ]
