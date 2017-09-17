# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-15 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=80)),
                ('city', models.CharField(max_length=40)),
                ('job', models.CharField(max_length=40)),
                ('bday', models.DateField()),
                ('password', models.CharField(max_length=80)),
                ('gender', models.CharField(max_length=25)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]