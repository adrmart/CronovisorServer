# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 17:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0010_auto_20160525_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='titulo',
            new_name='title',
        ),
    ]
