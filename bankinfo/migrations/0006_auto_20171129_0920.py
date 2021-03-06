# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankinfo', '0005_auto_20171129_0749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank',
            old_name='operating_time',
            new_name='operating_hours',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='brief_description',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='head_office_address',
        ),
        migrations.AddField(
            model_name='bank',
            name='about',
            field=models.TextField(blank=True, verbose_name='About '),
        ),
        migrations.AddField(
            model_name='bank',
            name='address',
            field=models.TextField(blank=True, verbose_name='Address '),
        ),
        migrations.AddField(
            model_name='bank',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email '),
        ),
        migrations.AddField(
            model_name='bank',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Phone Number '),
        ),
        migrations.AddField(
            model_name='bank',
            name='registered',
            field=models.CharField(blank=True, max_length=50, verbose_name='Registered '),
        ),
        migrations.AddField(
            model_name='bank',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
