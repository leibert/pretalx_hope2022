# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-29 15:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("mail", "0001_initial"),
        ("person", "0001_initial"),
        ("event", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="accept_template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="mail.MailTemplate",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="ack_template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="mail.MailTemplate",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="permitted",
            field=models.ManyToManyField(
                related_name="events",
                through="person.EventPermission",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="reject_template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="mail.MailTemplate",
            ),
        ),
    ]