from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard', views.MemberDashboard.as_view(),
         name='member-dashboard'),
]
