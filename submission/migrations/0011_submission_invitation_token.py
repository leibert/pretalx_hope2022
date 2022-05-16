# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import pretalx.submission.models.submission


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0010_auto_20171006_1118"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="invitation_token",
            field=models.CharField(
                default=pretalx.submission.models.submission.generate_invite_code,
                max_length=32,
            ),
        ),
    ]
