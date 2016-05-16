# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ajuda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('tema', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Duvida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('tema', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nome_usuario', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('dono', models.ForeignKey(related_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
