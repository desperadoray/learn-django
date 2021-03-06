# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161130232429 on 2017-01-17 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('relation', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary.Person'),
        ),
    ]
