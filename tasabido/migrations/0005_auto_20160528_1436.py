# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-28 14:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0004_auto_20160528_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duvida',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='monitoria',
            name='usuario',
        ),
    ]
