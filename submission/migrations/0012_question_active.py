# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0011_submission_invitation_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
