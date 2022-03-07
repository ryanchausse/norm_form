import datetime
import uuid

import requests
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
import reportlab
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http.response import FileResponse


class SubmitNormForm(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        if not self.request.user.groups.filter(name='Admins').exists():
            return redirect('/')
        context = self.get_context_data(**kwargs)
        # create a form instance and populate it with data from the request:
        form = NormFormForm(request.POST)
        if form.is_valid():
            # Save to DB
            form_to_save = form.save(commit=False)
            form_to_save.created_by = request.user
            form_to_save.filename = f'{form_to_save.date} - {form_to_save.patient} - ' \
                                    f'{form_to_save.facility} ' + str(uuid.uuid4()) + '.pdf'
            form_to_save.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully saved form')
            print('saved successfully')

            # Save to PDF
            print('Processing NormForm to PDF now... '
                  f'{form_to_save.name} - {form_to_save.patient} - {form_to_save.facility} - {form_to_save.date}')
            filename = form_to_save.filename
            pdf = canvas.Canvas(filename=os.path.abspath(os.path.dirname(__file__)) + '/patient_files/' + filename,
                                pagesize=letter)
            width, height = letter
            pdf.setLineWidth(.3)
            pdf.setFont('Helvetica', 12)
            pdf.setTitle(filename)
            pdf.drawString(30, 750, 'Norman Hendricksen. Ph.D.')
            pdf.drawString(500, 750, str(form_to_save.date))
            pdf.line(480, 747, 580, 747)
            pdf.drawString(275, 725, 'AMOUNT OWED:')
            pdf.drawString(500, 725, "$1,000.00")
            pdf.line(378, 723, 580, 723)
            pdf.drawString(30, 703, 'RECEIVED BY:')
            pdf.line(120, 700, 580, 700)
            pdf.drawString(120, 703, form_to_save.signature)
            pdf.setFont('Helvetica', 8)
            pdf.drawString(5, 5, f'Date: {form_to_save.date} Patient: {form_to_save.patient} '
                                 f'Facility: {form_to_save.facility} Time printed: {datetime.datetime.now()}')
            pdf.showPage()
            pdf.save()
            return redirect('/')
            # return FileResponse(open(filename, 'rb'), as_attachment=True, filename=f'{date} - {patient} - {facility}')
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

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='Admins').exists():
            context['user_is_in_admins'] = True
            if pk:
                norm_form = NormForm.objects.get(id=pk)
                form = NormFormForm(initial=model_to_dict(norm_form))
            else:
                form = NormFormForm()
            context['form'] = form
        else:
            context['user_is_in_admins'] = False
            context['form'] = None
        return context


class ViewNormFormsPage(TemplateView):
    """
    View previously submitted Norm Forms
    """
    template_name = 'view_norm_forms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='Admins').exists():
            context['user_is_in_admins'] = True
            context['norm_forms'] = NormForm.objects.all().order_by('-created_at')
        else:
            context['user_is_in_admins'] = False
            context['norm_forms'] = None
        return context


def get_pdf_page(request, pk=None):
    """
    Get PDF of a given NormForm via pk id
    """
    if request.user.groups.filter(name='Admins').exists() and pk:
        norm_form = NormForm.objects.get(id=pk)
        if norm_form.filename:
            # return file from patient_files as pdf response
            return FileResponse(open(os.path.abspath(os.path.dirname(__file__)) +
                                     '/patient_files/' +
                                     norm_form.filename, 'rb'), content_type='application/pdf')
    return redirect('/')


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
