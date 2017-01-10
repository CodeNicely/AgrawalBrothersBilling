# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-02 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=20, null=True)),
                ('firm_id', models.IntegerField()),
                ('firm_name', models.CharField(blank=True, max_length=255, null=True)),
                ('broker', models.CharField(blank=True, default='No Broker', max_length=255, null=True)),
                ('product_quantity', models.DecimalField(decimal_places=2, max_digits=20)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('truck_number', models.CharField(blank=True, max_length=32, null=True)),
                ('order_type', models.CharField(blank=True, max_length=10, null=True)),
                ('remark', models.CharField(blank=True, default='No Remark', max_length=255, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
