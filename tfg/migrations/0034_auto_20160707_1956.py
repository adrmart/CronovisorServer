# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-07 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0033_auto_20160705_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='orientation',
        ),
        migrations.AddField(
            model_name='image',
            name='signatura',
            field=models.CharField(max_length=25, null=True),
        ),
    ]