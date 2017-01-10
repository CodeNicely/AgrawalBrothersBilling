# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-02 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_data_firm_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_data',
            name='product_name',
            field=models.CharField(blank=True, choices=[('Bhusa', 'Bhusa'), ('Bhusi', 'Bhusi'), ('Filter Kodha', 'Filter Kodha'), ('Non Filter Kodha', 'Non Filter Kodha'), ('Combo Filter Kodha', 'Combo Filter Kodha'), ('Rafi', 'Rafi'), ('Kanki', 'Kanki'), ('Hallar Konda', 'Hallar Konda'), ('Badra', 'Badra')], max_length=20, null=True),
        ),
    ]
