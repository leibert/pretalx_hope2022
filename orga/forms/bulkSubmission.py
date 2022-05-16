from django import forms
from django.utils.translation import gettext as _
from django_scopes.forms import SafeModelChoiceField

from pretalx.common.mixins.forms import ReadOnlyFlag, RequestRequire
from pretalx.submission.models import Submission, SubmissionType


class BulkSubmissionForm(ReadOnlyFlag, RequestRequire, forms.ModelForm):
    def __init__(self, event, **kwargs):
        self.event = event
        super().__init__(**kwargs)
        self.fields["submission_type"].queryset = SubmissionType.objects.filter(
            event=event
        )

        if not event.settings.use_tracks:
            self.fields.pop("track")
        else:
            self.fields["track"].queryset = event.tracks.all()

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        return instance

    class Meta:
        model = Submission
        fields = [
            "submission_type",
            "track",
        ]
        field_classes = {
            "submission_type": SafeModelChoiceField,
            "track": SafeModelChoiceField,
        }
        request_require = {
        }
