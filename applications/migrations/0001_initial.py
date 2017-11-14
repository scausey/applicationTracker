# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 23:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('date_applied', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(max_length=200)),
                ('notes', models.TextField()),
            ],
        ),
    ]