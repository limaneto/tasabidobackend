# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-24 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monitoria',
            old_name='data',
            new_name='data_criacao',
        ),
        migrations.AlterField(
            model_name='monitoria',
            name='endereco',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
