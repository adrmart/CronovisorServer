# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0027_auto_20160613_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='num_images',
            field=models.IntegerField(default=1),
        ),
    ]
