# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 08:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='interview_date',
            new_name='interviewDate',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_type',
            new_name='questionType',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='bdate',
            new_name='birthDate',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='fname',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='groupid',
            new_name='groupId',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lname',
            new_name='lastName',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='ldate',
            new_name='loginDate',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userid',
            new_name='userId',
        ),
    ]
