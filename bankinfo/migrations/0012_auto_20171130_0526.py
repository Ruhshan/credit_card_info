# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 05:26
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankinfo', '0011_auto_20171130_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='address',
        ),
        migrations.AddField(
            model_name='branch',
            name='location',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, verbose_name='Location '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='services',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, verbose_name='Services '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status '),
        ),
    ]
