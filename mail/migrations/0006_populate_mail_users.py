# Generated by Django 2.1.7 on 2019-03-27 21:35

from django.db import migrations


def populate_to_users(apps, schema_editor):
    QueuedMail = apps.get_model("mail", "QueuedMail")
    User = apps.get_model("person", "User")
    user_lookup = {
        user.email.lower().strip(): user for user in User.objects.all() if user.email
    }
    for mail in QueuedMail.objects.all():
        addresses = []
        for address in (mail.to or "").split(","):
            address = address.lower().strip()
            if address:
                addresses.append(address)
        for address in addresses:
            user = user_lookup.get(address)
            if user:
                addresses.remove(address)
                mail.to_users.add(user)
        mail.to = ",".join(addresses)
        mail.save()


def depopulate_to_users(apps, schema_editor):
    QueuedMail = apps.get_model("mail", "QueuedMail")
    for mail in QueuedMail.objects.filter(to_users__isnull=False):
        addresses = [user.email for user in mail.to_users.all()] + (
            mail.to or ""
        ).split(",")
        mail.to_users.clear()
        if addresses:
            mail.to = ",".join(addresses)
            mail.save()


class Migration(migrations.Migration):

    dependencies = [
        ("mail", "0005_queuedmail_to_users"),
        ("person", "0020_auto_20180922_0511"),
    ]

    operations = [
        migrations.RunPython(populate_to_users, depopulate_to_users),
    ]