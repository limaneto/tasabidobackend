# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-30 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0004_auto_20160530_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoria',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, default=222.222, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='monitoria',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=6, default=222.222, max_digits=9, null=True),
        ),
    ]
