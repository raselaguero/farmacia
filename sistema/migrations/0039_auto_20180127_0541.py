# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-27 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_Gestion_Medicamentos', '0038_auto_20180127_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devueltocama',
            name='justificacion',
            field=models.CharField(choices=[('TRASLADO', 'TRASLADO'), ('EGRESO', 'EGRESO'), ('OTRA', 'OTRA'), ('FALLECIMIENTO', 'FALLECIMIENTO'), ('CAMBIO DE TRATAMIENTO', 'CAMBIO DE TRATAMIENTO')], max_length=40),
        ),
        migrations.AlterField(
            model_name='devueltofarmacia',
            name='justificacion',
            field=models.CharField(choices=[('RETENIDO', 'RETENIDO'), ('MAL ESTADO', 'MAL ESTADO'), ('DISMINUCION DEL FONDO FIJO', 'DISMINUCION DEL FONDO FIJO'), ('VENCIMIENTO', 'VENCIMIENTO')], max_length=40),
        ),
        migrations.AlterField(
            model_name='tarjetaestibadetalle',
            name='fecha',
            field=models.DateField(),
        ),
    ]