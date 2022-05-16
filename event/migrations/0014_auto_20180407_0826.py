# Generated by Django 2.0.3 on 2018-04-07 13:26

from django.db import migrations


def create_team(permissions, apps, event, reviewer, orga):
    Team = apps.get_model("event", "Team")
    TeamInvite = apps.get_model("event", "TeamInvite")
    name = str(event.name) + (" Organisers" if orga else " Reviewers")
    if orga and reviewer:
        name += " and reviewers"
    team = Team.objects.create(
        organiser=event.organiser,
        name=name,
        can_create_events=orga,
        can_change_teams=orga,
        can_change_organiser_settings=orga,
        can_change_event_settings=orga,
        can_change_submissions=orga,
        is_reviewer=reviewer,
    )
    team.limit_events.add(event)
    for perm in permissions:
        if perm.user:
            team.members.add(perm.user)
        else:
            TeamInvite.objects.create(
                team=team, email=perm.invitation_email, token=perm.invitation_token
            )
    team.save()


def build_teams(event, apps):
    orga_only_permissions = []
    reviewer_only_permissions = []
    both_permissions = []
    for perm in event.permissions.all():
        if perm.is_orga and perm.is_reviewer:
            both_permissions.append(perm)
        elif perm.is_orga:
            orga_only_permissions.append(perm)
        elif perm.is_reviewer:
            reviewer_only_permissions.append(perm)
    if orga_only_permissions:
        create_team(orga_only_permissions, apps, event, reviewer=False, orga=True)
    if reviewer_only_permissions:
        create_team(reviewer_only_permissions, apps, event, reviewer=True, orga=False)
    if both_permissions:
        create_team(both_permissions, apps, event, reviewer=True, orga=True)


def build_organisers(apps, schema_editor):
    Event = apps.get_model("event", "Event")
    Organiser = apps.get_model("event", "Organiser")
    for event in Event.objects.all():
        organiser = Organiser.objects.create(
            name=str(event.name) + " Organiser",
            slug=event.slug + "org",
        )
        event.organiser = organiser
        event.save()
        build_teams(event, apps)


def remove_organisers(apps, schema_editor):
    Organiser = apps.get_model("event", "Organiser")
    Team = apps.get_model("event", "Team")
    Team.objects.all().delete()
    for organiser in Organiser.objects.all():
        for event in organiser.events.all():
            event.organiser = None
            event.save()
    Organiser.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0013_auto_20180407_0817"),
    ]

    operations = [
        migrations.RunPython(code=build_organisers, reverse_code=remove_organisers),
    ]
