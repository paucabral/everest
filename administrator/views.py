from django.core.exceptions import EmptyResultSet
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages

# Create your views here.


class AdministratorDashboard(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        return render(request, template_name='administrator/dashboard.html', context={})


class CreateEvent(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        form = EventForm()
        return render(request, template_name='administrator/event-form.html', context={'form': form})

    @method_decorator(login_required(login_url='/'))
    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()

            messages.add_message(request,
                                 messages.SUCCESS,
                                 'The event was added successfully.')
            return redirect('/administrator/events/list')
        else:
            messages.error(request, 'The event was not added due to an error.')
            return render(request, template_name='administrator/event-form.html', context={'form': form})


class UpdateEvent(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        event_id = self.kwargs['event_id']
        event = Event.objects.get(pk=event_id)

        form = EventForm(instance=event)
        return render(request, template_name='administrator/event-form.html', context={'form': form})

    @method_decorator(login_required(login_url='/'))
    def post(self, request, *args, **kwargs):
        event_id = self.kwargs['event_id']
        event = Event.objects.get(pk=event_id)

        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()

            messages.add_message(request,
                                 messages.SUCCESS,
                                 'The event was added successfully.')
            return redirect('/administrator/events/list')
        else:
            messages.error(
                request, 'The event was not updated due to an error.')
            return render(request, template_name='administrator/event-form.html', context={'form': form})


class ListEvents(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        events = Event.objects.all().order_by('-date')
        return render(request, template_name='administrator/list-events.html', context={'events': events})

    @method_decorator(login_required(login_url='/'))
    def post(self, request, *args, **kwargs):
        pass
