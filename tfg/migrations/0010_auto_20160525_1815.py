# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0009_auto_20160525_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
    ]
