# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 07:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankinfo', '0002_branches'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Branches',
            new_name='Branche',
        ),
    ]
