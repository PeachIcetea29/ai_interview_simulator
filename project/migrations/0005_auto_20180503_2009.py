# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20180503_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birthDate',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='firstName',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='groupId',
            field=models.IntegerField(default=5, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastName',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='loginDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]