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
from .forms import NormFormForm
from django.contrib.auth import get_user_model
from django.contrib import messages


class SubmitNormForm(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # create a form instance and populate it with data from the request:
        form = NormFormForm(request.POST)
        if form.is_valid():
            form_to_save = form.save(commit=False)
            form_to_save.created_by = request.user
            form_to_save.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully saved form')
            print('saved successfully')
            return redirect('/')
        else:
            print('form is not valid')
            print(form.errors)
            messages.add_message(request, messages.WARNING, 'Form not valid')
        # request.session.flush()
        return redirect('/')


class NormFormPage(TemplateView):
    """
    First / Login page at root
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='Admins').exists():
            context['user_is_in_admins'] = True
        else:
            context['user_is_in_admins'] = False
        form = NormFormForm()
        context['form'] = form
        return context


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
