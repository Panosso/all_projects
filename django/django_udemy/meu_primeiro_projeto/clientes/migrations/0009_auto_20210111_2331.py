# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-01-11 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_auto_20210111_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpf',
            name='data_exp',
            field=models.DateTimeField(),
        ),
    ]
