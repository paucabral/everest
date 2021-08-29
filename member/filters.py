import django_filters
from django_filters import CharFilter
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
