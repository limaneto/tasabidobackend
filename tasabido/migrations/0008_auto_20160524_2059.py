# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-24 20:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0007_auto_20160524_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monitoria',
            old_name='data_criacao',
            new_name='data_monitoria',
        ),
    ]