# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0009_auto_20171001_0433"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="capacity",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="description",
            field=i18nfield.fields.I18nCharField(
                blank=True, max_length=1000, null=True
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="name",
            field=i18nfield.fields.I18nCharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="room",
            name="position",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="version",
            field=models.CharField(blank=True, max_length=190, null=True),
        ),
    ]