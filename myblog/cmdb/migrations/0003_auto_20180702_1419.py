# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-02 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cmdb', '0002_auto_20161203_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsernameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('pwd', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('gender', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_type',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
