from django.core.exceptions import EmptyResultSet
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .decorators import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from accounts.models import Profile, User
from django.db.models import Q
from member.models import Event, EventRegistration
from member.filters import FindEventFilter, EventsJoinedFilter

# Create your views here.


class AdministratorDashboard(View):
    @method_decorator(login_required(login_url='/'))
    @method_decorator(admin_only())
    def get(self, request, *args, **kwargs):
        return render(request, template_name='administrator/dashboard.html', context={})


class CreateEvent(View):
    @method_decorator(login_required(login_url='/'))
    @method_decorator(admin_only())
    def get(self, request, *args, **kwargs):
        form = EventForm()
        return render(request, template_name='administrator/event-form.html', context={'form': form})

    @method_decorator(login_required(login_url='/'))
    @method_decorator(admin_only())
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
    @method_decorator(admin_only())
    def get(self, request, *args, **kwargs):
        event_id = self.kwargs['event_id']
        event = Event.objects.get(pk=event_id)

        form = EventForm(instance=event)
        return render(request, template_name='administrator/event-form.html', context={'form': form})

    @method_decorator(login_required(login_url='/'))
    @method_decorator(admin_only())
    def post(self, request, *args, **kwargs):
        event_id = self.kwargs['event_id']
        event = Event.objects.get(pk=event_id)

        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()

            messages.add_message(request,
                                 messages.SUCCESS,
                                 'The event was updated successfully.')
            return redirect('/administrator/events/list')
        else:
            messages.error(
                request, 'The event was not updated due to an error.')
            return render(request, template_name='administrator/event-form.html', context={'form': form})


class ListEvents(View):
    @method_decorator(login_required(login_url='/'))
    @method_decorator(admin_only())
    def get(self, request, *args, **kwargs):
        events = Event.objects.all().order_by('-date')
        return render(request, template_name='administrator/list-events.html', context={'events': events})


@login_required(login_url='/')
@admin_only()
def deleteEvent(request, event_id):
    if request.method == "POST":
        event = Event.objects.filter(id=event_id)
        event.delete()

        messages.add_message(request,
                             messages.SUCCESS,
                             'The event was deleted successfully.')
        return redirect('/administrator/events/list')

    return redirect('/administrator/events/list')


class ListMembers(View):
    @method_decorator(login_required(login_url='/'))
    @method_decorator(admin_only())
    def get(self, request, *args, **kwargs):
        registered_events = EventRegistration.objects.exclude(
            time_of_attendance__isnull=True)

        members = User.objects.exclude(
            Q(is_superuser=True)).order_by('-last_name')
        return render(request, template_name='administrator/list-members.html', context={'members': members, 'registered_events': registered_events})


@login_required(login_url='/')
@admin_only()
def deleteMember(request, member_id):
    if request.method == "POST":
        user = User.objects.filter(id=member_id)
        user.delete()

        messages.add_message(request,
                             messages.SUCCESS,
                             'The user was deleted successfully.')
        return redirect('/administrator/members/list')

    return redirect('/administrator/members/list')


class AllTransactions(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        transactions = EventRegistration.objects.all().order_by('-date_created')

        transactions_filter = EventsJoinedFilter(
            request.GET, queryset=transactions)
        transactions = transactions_filter.qs

        return render(request, template_name='administrator/transactions.html', context={'transactions': transactions, 'transactions_filter': transactions_filter})
