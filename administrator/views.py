from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


class AdministratorDashboard(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Administrator Dashboard')

    def post(self, request, *args, **kwargs):
        pass
