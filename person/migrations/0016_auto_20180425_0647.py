# Generated by Django 2.0.3 on 2018-04-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("person", "0015_speakerinformation_resource"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(default="", max_length=120),
            preserve_default=False,
        ),
    ]