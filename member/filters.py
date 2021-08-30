import django_filters
from django_filters import CharFilter, ChoiceFilter
from .models import *
from django import forms
from administrator.models import *


class FindEventFilter(django_filters.FilterSet):
    name = CharFilter(field_name='event_name', lookup_expr='icontains')

    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['event_name', 'short_description', 'detailed_description',
                   'is_registration_open', 'is_attendance_open']


class EventsJoinedFilter(django_filters.FilterSet):
    name = CharFilter(field_name='event__event_name', lookup_expr='icontains')
    cost = ChoiceFilter(field_name='event__cost', choices=Event.EVENT_COST)
    event_type = ChoiceFilter(field_name='event__event_type',
                              choices=Event.EVENT_TYPE)
    approval = ChoiceFilter(field_name='is_registration_approved',
                            choices=EventRegistration.APPROVAL)

    class Meta:
        model = EventRegistration
        fields = '__all__'
        exclude = ['time_of_attendance', 'receipt']
