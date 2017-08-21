# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0016_remove_cart_items_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_items',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='數量'),
        ),
    ]
