# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0011_auto_20160517_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ajuda',
            name='tema',
        ),
        migrations.RemoveField(
            model_name='duvida',
            name='tema',
        ),
    ]
