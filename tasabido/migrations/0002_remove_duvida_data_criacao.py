# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-29 00:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duvida',
            name='data_criacao',
        ),
    ]
