# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-24 17:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Duvida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('data_criacao', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Monitoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('data', models.DateField(null=True)),
                ('hora', models.DateTimeField(null=True)),
                ('endereco', models.CharField(max_length=200)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('materia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasabido.Materia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subtopico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('materia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasabido.Materia')),
            ],
        ),
        migrations.AddField(
            model_name='monitoria',
            name='subtopico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasabido.Subtopico'),
        ),
        migrations.AddField(
            model_name='monitoria',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='duvida',
            name='materia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasabido.Materia'),
        ),
        migrations.AddField(
            model_name='duvida',
            name='subtopico',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasabido.Subtopico'),
        ),
        migrations.AddField(
            model_name='duvida',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
