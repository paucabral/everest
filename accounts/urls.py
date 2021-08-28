from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
]
