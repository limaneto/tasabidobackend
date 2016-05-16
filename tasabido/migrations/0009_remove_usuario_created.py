# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0008_auto_20160514_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='created',
        ),
    ]
