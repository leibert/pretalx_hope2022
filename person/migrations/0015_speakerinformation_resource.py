# Generated by Django 2.0.2 on 2018-03-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("person", "0014_speakerinformation"),
    ]

    operations = [
        migrations.AddField(
            model_name="speakerinformation",
            name="resource",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]