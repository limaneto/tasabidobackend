# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-24 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasabido', '0005_auto_20160524_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duvida',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasabido.Materia'),
        ),
        migrations.AlterField(
            model_name='duvida',
            name='subtopico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasabido.Subtopico'),
        ),
        migrations.AlterField(
            model_name='monitoria',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasabido.Materia'),
        ),
        migrations.AlterField(
            model_name='subtopico',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasabido.Materia'),
        ),
    ]