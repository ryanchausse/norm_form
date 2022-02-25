from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import RequestContext
from django.core import serializers
from django.forms.models import model_to_dict
import logging
from django.conf import settings
from .models import Patient
from .models import NormForm


class SubmitNormForm(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        request.session.flush()
        return redirect('/index.html')


class NormFormPage(TemplateView):
    """
    First / Login page at root
    """
    template_name = 'index.html'


class ManagerPage(TemplateView):
    """
    Front desk / manager page to list normforms
    """
    template_name = 'manager.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.groups.filter(name='Admins').exists():
            context = self.get_context_data(**kwargs)
            context['norm_forms'] = NormForm.objects.all().order_by('-created_at')
            return render(request,
                          template_name=self.template_name,
                          context=context)
        else:
            return redirect('/index.html')


def handler404(request, exception, template_name="404.html"):
    """
    Custom 404 page
    """
    response = render(template_name)
    response.status_code = 404
    return response


def handler500(request, exception, template_name="500.html"):
    """
    Custom 500 page
    """
    response = render(template_name)
    response.status_code = 500
    return response
