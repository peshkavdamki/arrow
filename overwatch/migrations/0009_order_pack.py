# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-06 04:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overwatch', '0008_auto_20180505_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='overwatch.Pack'),
        ),
    ]
