# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 08:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0015_auto_20170819_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_items',
            name='quantity',
        ),
    ]
