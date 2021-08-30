from django.forms import ModelForm
from django import forms
from .models import *


class EventRegistrationForm(ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['user', 'event', 'receipt', 'is_registration_approved']

    def __init__(self, *args, **kwargs):
        super(EventRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['user'].widget.attrs.update(
            {'type': 'hidden', 'style': 'display: none;'})
        self.fields['event'].widget.attrs.update(
            {'type': 'hidden', 'style': 'display: none;'})
        self.fields['is_registration_approved'].widget.attrs.update(
            {'type': 'hidden', 'style': 'display: none;'})
        self.fields['receipt'].widget.attrs.update(
            {'class': 'form-control upload-image-receipt'})
