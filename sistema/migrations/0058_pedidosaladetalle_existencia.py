# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-20 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_Gestion_Medicamentos', '0057_sala_secretaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidosaladetalle',
            name='existencia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Sistema_Gestion_Medicamentos.Existencia'),
            preserve_default=False,
        ),
    ]