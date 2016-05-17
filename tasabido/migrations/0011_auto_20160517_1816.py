# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0010_auto_20160517_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajuda',
            name='usuario',
            field=models.ForeignKey(to='tasabido.Usuario'),
        ),
        migrations.AlterField(
            model_name='duvida',
            name='usuario',
            field=models.ForeignKey(to='tasabido.Usuario'),
        ),
    ]
