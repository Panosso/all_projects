# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-01-06 20:42
from __future__ import unicode_literals

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='idade',
            field=models.IntegerField(default=builtins.print, max_length=100),
            preserve_default=False,
        ),
    ]
