# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterFlow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('flow', models.FloatField()),
                ('date', models.DateTimeField(unique=True)),
            ],
            options={
                'db_table': 'water_flow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WaterLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.FloatField()),
                ('date', models.DateTimeField(unique=True)),
            ],
            options={
                'db_table': 'water_level',
                'managed': False,
            },
        ),
    ]