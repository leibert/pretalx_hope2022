# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 23:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pretalx.common.mixins


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("submission", "0002_auto_20170820_1216"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("rating", models.IntegerField(blank=True, null=True)),
                ("review", models.TextField()),
                (
                    "speaker",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="feedback",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=(pretalx.common.mixins.models.LogMixin, models.Model),
        ),
        migrations.AddField(
            model_name="submission",
            name="accept_feedback",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="submission",
            name="do_not_record",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="feedback",
            name="talk",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="feedback",
                to="submission.Submission",
            ),
        ),
    ]