# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.CharField(max_length=13, verbose_name='National ID')),
                ('name_on_card', models.CharField(max_length=127, verbose_name='Name On card')),
                ('card_number', models.CharField(max_length=127, verbose_name='Card Number')),
                ('expire_on', models.DateField(verbose_name='Expire On')),
                ('card_cif', models.CharField(max_length=127, verbose_name='Card CIF')),
                ('card_cvv', models.CharField(max_length=127, verbose_name='CVV')),
                ('bank_cif', models.CharField(max_length=127, verbose_name='Bank CIF')),
            ],
        ),
    ]
