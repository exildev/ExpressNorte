# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0003_auto_20151224_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='identificacion',
            field=models.CharField(unique=True, max_length=15, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'identificacion no valida', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_celular',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'telefono no valido', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_fijo',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'telefono no valido', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nit',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'numero no valida')]),
        ),
        migrations.AlterField(
            model_name='motorizado',
            name='licencia',
            field=models.CharField(unique=True, max_length=50, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'licencia no valida', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='soat',
            name='numeroS',
            field=models.CharField(unique=True, max_length=50, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'numero no valida', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='tecno',
            name='numeroT',
            field=models.CharField(unique=True, max_length=50, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'numero no valida', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='identificacion',
            field=models.CharField(unique=True, max_length=15, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'identificacion no valida', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono_celular',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'telefono no valido', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono_fijo',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(re.compile(b'^[0-9]+$'), b'telefono no valido', b'invalid')]),
        ),
    ]
