# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankinfo', '0009_auto_20171129_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='details',
        ),
        migrations.AddField(
            model_name='bankdetails',
            name='bank',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='bankinfo.Bank', verbose_name='Details'),
        ),
    ]
