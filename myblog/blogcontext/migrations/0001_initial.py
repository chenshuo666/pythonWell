# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-13 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=1024)),
                ('article_type',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogcontext.ArticleType')),
            ],
        ),
        migrations.CreateModel(
            name='Category_Blog_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='blog_article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='blogcontext.Category_Blog_article'),
        ),
    ]
