# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170925_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('text', models.TextField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
