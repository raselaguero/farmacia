# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-27 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_Gestion_Medicamentos', '0010_auto_20180126_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='devuelto',
            name='justificacion',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]