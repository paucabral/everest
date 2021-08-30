from django.db.models import query
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from administrator.models import Event
from .models import *
from .filters import *
from django.contrib import messages
from django.utils import timezone
import datetime

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
        user = Profile.objects.get(id=request.user.profile.id)
        user_registered_events = EventRegistration.objects.filter(
            user=user).values_list('event_id', flat=True)

        find_event_filter = FindEventFilter(request.GET, queryset=events)
        events = find_event_filter.qs

        return render(request, template_name='member/find-event.html', context={'events': events, 'user_registered_events': user_registered_events, 'find_event_filter': find_event_filter})


class ViewEvent(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        event_id = self.kwargs['event_id']
        event = Event.objects.get(pk=event_id)
        user = Profile.objects.get(id=request.user.profile.id)

        user_registered_events = EventRegistration.objects.filter(
            user=user).values_list('event_id', flat=True)

        return render(request, template_name='member/event-details.html', context={'event': event, 'user_registered_events': user_registered_events})


@login_required(login_url='/')
def registerEvent(request, event_id):
    if request.method == "POST":
        user = Profile.objects.get(id=request.user.profile.id)
        event = Event.objects.get(id=event_id)
        time = timezone.now()

        if event.cost == "FREE":
            approval = True
            new_event_registration = EventRegistration.objects.create(
                user=user, event=event, time_of_attendance=time, is_registration_approved=approval)

            messages.add_message(request,
                                 messages.SUCCESS,
                                 'You have successfully registered on the event.')
            return redirect("/member/events/event/{}".format(event_id))

        else:
            return redirect('/')


@login_required(login_url='/')
def unregisterEvent(request, event_id):
    if request.method == "POST":
        user = Profile.objects.get(id=request.user.profile.id)
        event = Event.objects.get(id=event_id)

        event_registered = EventRegistration.objects.filter(
            user=user, event=event)

        event_registered.delete()
        messages.add_message(request,
                             messages.SUCCESS,
                             'You have successfully unregistered from the event.')
        return redirect("/member/events/event/{}".format(event_id))
