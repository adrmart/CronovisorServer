# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0003_auto_20160518_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='street',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='street',
            name='represent',
            field=models.IntegerField(null=True),
        ),
    ]