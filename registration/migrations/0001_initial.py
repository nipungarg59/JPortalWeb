# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment', models.CharField(max_length=10)),
                ('cookie', models.CharField(max_length=1000)),
            ],
        ),
    ]