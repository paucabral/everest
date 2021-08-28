from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.AdministratorDashboard.as_view(),
         name='administrator-dashboard'),
    path('events/create-new', views.CreateEvent.as_view(),
         name='create-event'),
]
