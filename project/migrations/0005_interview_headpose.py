# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-01 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_interview_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='headpose',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
