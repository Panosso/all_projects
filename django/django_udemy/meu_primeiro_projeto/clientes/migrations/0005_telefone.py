# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-01-11 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20210106_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=1000)),
            ],
        ),
    ]
