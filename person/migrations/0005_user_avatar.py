# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("person", "0004_auto_20171001_1358"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
