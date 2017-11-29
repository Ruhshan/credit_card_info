# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=127, verbose_name='Branch Name ')),
                ('branch_address', models.TextField(verbose_name='Branch Address')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankinfo.Bank', verbose_name='Bank ')),
            ],
        ),
    ]
