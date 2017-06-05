from django import forms
from django.forms.models import modelform_factory

from .models import Participant, Talk

ParticipantForm = modelform_factory(Participant, fields=['name', 'email', 'phone_number', 'biography'])
TalkForm = modelform_factory(Talk, fields=['title', 'description', 'notes'])


class ProposeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProposeForm, self).__init__(*args, **kwargs)
        # Participant
        self.participant_form = ParticipantForm(*args, **kwargs)
        self.fields.update(self.participant_form.fields)
        self.initial.update(self.participant_form.initial)
        # Talk
        self.talk_form = TalkForm(*args, **kwargs)
        self.fields.update(self.talk_form.fields)
        self.initial.update(self.talk_form.initial)

    def is_valid(self):
        isValid = True
        if not self.participant_form.is_valid() or not self.talk_form.is_valid():
            isValid = False
        if not super(ProposeForm, self).is_valid():
            isValid = False
        self.errors.update(self.participant_form.errors)
        self.errors.update(self.talk_form.errors)
        return isValid

    def clean(self):
        cleaned_data = super(ProposeForm, self).clean()
        cleaned_data.update(self.participant_form.cleaned_data)
        cleaned_data.update(self.talk_form.cleaned_data)
        return cleaned_data
