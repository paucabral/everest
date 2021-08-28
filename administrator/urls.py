from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.AdministratorDashboard.as_view(),
         name='administrator-dashboard'),
]
