# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-08-07 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vgc',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]