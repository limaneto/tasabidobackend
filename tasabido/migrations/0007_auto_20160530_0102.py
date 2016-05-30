# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-30 01:02
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0006_auto_20160530_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoria',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=Decimal('0.00'), max_digits=9),
        ),
        migrations.AlterField(
            model_name='monitoria',
            name='long',
            field=models.DecimalField(decimal_places=6, default=Decimal('0.00'), max_digits=9),
        ),
    ]
