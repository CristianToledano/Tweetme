# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_tweet_miriam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='miriam',
        ),
    ]