# Generated by Django 2.0.3 on 2018-04-07 13:14

import django.core.validators
from django.db import migrations, models
import pretalx.event.models.event


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0011_event_question_template"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={"ordering": ("date_from",)},
        ),
        migrations.AlterField(
            model_name="event",
            name="custom_css",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=pretalx.event.models.event.event_css_path,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="primary_color",
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="slug",
            field=models.SlugField(
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="The slug may only contain letters, numbers, dots and dashes.",
                        regex="^[a-zA-Z0-9.-]+$",
                    ),
                    pretalx.event.models.event.validate_event_slug_permitted,
                ],
            ),
        ),
    ]
