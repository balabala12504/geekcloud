# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20160817_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(help_text='* required', to='users.UserGroup', verbose_name='\u7528\u6237\u7ec4'),
        ),
    ]
