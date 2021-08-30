from administrator.models import Event
from django.db import models
from accounts.models import Profile
from administrator.models import Event

# Create your models here.


class EventRegistration(models.Model):
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE)
    is_registration_approved = models.BooleanField(null=False)
    time_of_attendance = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return self.user.user.username + "+" + self.event.event_name
