# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0007_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Materia',
        ),
        migrations.RenameField(
            model_name='materia',
            old_name='username',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='owner',
        ),
    ]
