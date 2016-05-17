# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0009_remove_usuario_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='ajuda',
            name='usuario',
            field=models.ForeignKey(default=1, to='tasabido.Usuario'),
        ),
        migrations.AddField(
            model_name='duvida',
            name='usuario',
            field=models.ForeignKey(default=1, to='tasabido.Usuario'),
        ),
    ]
