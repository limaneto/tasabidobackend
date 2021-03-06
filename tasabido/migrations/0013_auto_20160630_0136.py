# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-30 01:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasabido', '0012_auto_20160623_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moeda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantia', models.IntegerField(default=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='user',
        ),
        migrations.RemoveField(
            model_name='monitoria',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='monitoria',
            name='long',
        ),
        migrations.RemoveField(
            model_name='monitoria',
            name='segunda_data_monitoria',
        ),
        migrations.RemoveField(
            model_name='monitoria',
            name='terceira_data_monitoria',
        ),
        migrations.AddField(
            model_name='monitoria',
            name='dia',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monitoria',
            name='horario',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monitoria',
            name='username',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='duvida',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='monitoria',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Aluno',
        ),
    ]
