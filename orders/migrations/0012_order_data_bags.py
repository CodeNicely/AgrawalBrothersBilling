# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-02 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20170102_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_data',
            name='bags',
            field=models.IntegerField(default=0),
        ),
    ]
