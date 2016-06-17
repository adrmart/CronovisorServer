# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0004_auto_20160520_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='type',
            field=models.CharField(choices=[('SIN', '- Ninguno -'), ('CALLE', 'Calle'), ('AVENIDA', 'Avenida'), ('CALLEJON', 'Callejon'), ('CAMINO', 'Camino'), ('PASEO', 'Paseo'), ('TRAVESIA', 'Travesia'), ('PLAZA', 'Plaza'), ('PASADIZO', 'Pasadizo')], default='CALLE', max_length=30),
        ),
    ]
