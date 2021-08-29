from django.forms import ModelForm
from django import forms
from .models import *
from bootstrap_datepicker_plus import DateTimePickerInput


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': DateTimePickerInput
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        self.fields['event_name'].widget.attrs.update(
            {'class': 'form-control', 'required': 'required', 'autofocus': 'autofocus'})
        self.fields['short_description'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['location'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['detailed_description'].widget.attrs.update(
            {'class': 'form-control django-ckeditor-widget', })
        self.fields['event_type'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['date'].widget.attrs.update(
            {'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1'})
        self.fields['is_attendance_open'].widget.attrs.update(
            {'class': '', })
        self.fields['is_registration_open'].widget.attrs.update(
            {'class': '', })
        self.fields['cost'].widget.attrs.update(
            {'class': 'form-control', 'onchange': 'displayDivDemo(this)'})
        self.fields['price'].widget.attrs.update(
            {'class': 'form-control', })
