# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0009_remove_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='estore.Product'),
        ),
    ]
