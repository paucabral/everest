from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.AdministratorDashboard.as_view(),
         name='administrator-dashboard'),
    path('events/create-new', views.CreateEvent.as_view(),
         name='create-event'),
    path('events/list', views.ListEvents.as_view(),
         name='list-events'),
    path('events/update/<int:event_id>/',
         views.UpdateEvent.as_view(), name='update-event'),
    path('events/delete/<int:event_id>', views.deleteEvent, name='delete-event'),
]
