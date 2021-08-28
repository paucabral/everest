from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


class AdministratorDashboard(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        return render(request, template_name='administrator/dashboard.html', context={})

    @method_decorator(login_required(login_url='/'))
    def post(self, request, *args, **kwargs):
        pass
