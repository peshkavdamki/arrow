# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-05 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwatch', '0007_auto_20180505_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='newScore',
            field=models.PositiveSmallIntegerField(blank=True, default=1500, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='oldScore',
            field=models.PositiveSmallIntegerField(blank=True, default=1499, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(choices=[('B', 'boost'), ('Q', 'qualification')], max_length=1),
        ),
    ]
