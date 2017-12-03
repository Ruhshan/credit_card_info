# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 06:43
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankinfo', '0012_auto_20171130_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='bankinfo.Bank', verbose_name='Bank '),
        ),
        migrations.AlterField(
            model_name='branch',
            name='services',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Services '),
        ),
    ]