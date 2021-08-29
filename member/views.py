from django.db.models import query
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from administrator.models import Event
from .models import *
from .filters import *

# Create your views here.


class MemberDashboard(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        return render(request, template_name='member/dashboard.html', context={})


class FindEvent(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        events = Event.objects.filter(
            is_registration_open=True).order_by('date')

        find_event_filter = FindEventFilter(request.GET, queryset=events)
        events = find_event_filter.qs

        return render(request, template_name='member/find-event.html', context={'events': events, 'find_event_filter': find_event_filter})


class ViewEvent(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        event_id = self.kwargs['event_id']
        event = Event.objects.get(pk=event_id)

        return render(request, template_name='member/event-details.html', context={'event': event})
