# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-01-06 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20210106_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='idade',
            field=models.IntegerField(),
        ),
    ]
