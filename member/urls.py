from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard', views.MemberDashboard.as_view(),
         name='member-dashboard'),
    path('events/find', views.FindEvent.as_view(),
         name='find-event'),
    path('events/event/<int:event_id>', views.ViewEvent.as_view(),
         name='view-event'),
]
