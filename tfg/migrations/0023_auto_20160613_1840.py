# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0022_auto_20160613_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='represent',
            field=models.CharField(default=b'a', max_length=120),
        ),
    ]
