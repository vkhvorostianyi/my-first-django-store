# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_productinbasket'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductInBasket',
            new_name='ProductInCard',
        ),
    ]
