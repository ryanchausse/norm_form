import datetime
import uuid
import json
import requests
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
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
from reportlab.pdfbase.pdfmetrics import stringWidth
from django.http.response import FileResponse
from django.http.response import JsonResponse
from . import flowable_form_builder
from .models import SubjectiveBoilerplateOption
from .models import SubjectiveOption
from .models import DiscussionTreatmentOption
from .models import Icd10Codes


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
            filename = os.path.abspath(os.path.dirname(__file__)) + '/patient_files/' + form_to_save.filename
            # pdf = canvas.Canvas(filename=os.path.abspath(os.path.dirname(__file__)) + '/patient_files/' + filename,
            #                     pagesize=letter)
            flowable_form_builder.build_form(form_to_save=form_to_save, filename=filename)
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


def get_subjective_boilerplate_option_text(request):
    """
    Get value of a given SubjectiveBoilerplateOption via $.AJAX in main_card
    """
    if not request.user.groups.filter(name='Admins').exists():
        return redirect('/')
    if 'ids' in request.GET and request.GET.get('ids'):
        ids = request.GET.get('ids').split(',')
    else:
        return JsonResponse('', safe=False)
    if request.is_ajax():
        subjective_boilerplate_options = SubjectiveBoilerplateOption.objects.filter(id__in=ids)
        response_text = ''
        for subjective_boilerplate_option in subjective_boilerplate_options:
            if subjective_boilerplate_option.full_text:
                response_text += subjective_boilerplate_option.full_text + ' '
        return JsonResponse(response_text, safe=False)
    return redirect('/')


def get_subjective_option_text(request):
    """
    Get value of a given SubjectiveOption via $.AJAX in main_card
    """
    if not request.user.groups.filter(name='Admins').exists():
        return redirect('/')
    if 'ids' in request.GET and request.GET.get('ids'):
        ids = request.GET.get('ids').split(',')
    else:
        return JsonResponse('', safe=False)
    if request.is_ajax():
        subjective_options = SubjectiveOption.objects.filter(id__in=ids)
        response_text = ''
        for subjective_option in subjective_options:
            if subjective_option.full_text:
                response_text += subjective_option.full_text + ' '
        return JsonResponse(response_text, safe=False)
    return redirect('/')


def get_discussion_treatment_option_text(request):
    """
    Get value of a given DiscussionTreatmentOption via $.AJAX() in main_card
    """
    if not request.user.groups.filter(name='Admins').exists():
        return redirect('/')
    if 'ids' not in request.GET or request.GET.get('ids'):
        ids = request.GET.get('ids').split(',')
    else:
        return JsonResponse('', safe=False)
    if request.is_ajax():
        discussion_treatment_options = DiscussionTreatmentOption.objects.filter(id__in=ids)
        response_text = ''
        for discussion_treatment_option in discussion_treatment_options:
            if discussion_treatment_option.full_text:
                response_text += discussion_treatment_option.full_text + ' '
        return JsonResponse(response_text, safe=False)
    return redirect('/')


def get_icd_10_code_text(request):
    """
    Get value of a given SubjectiveOption via $.AJAX in main_card
    """
    if not request.user.groups.filter(name='Admins').exists():
        return redirect('/')
    if 'ids' in request.GET and request.GET.get('ids'):
        ids = request.GET.get('ids').split(',')
    else:
        return JsonResponse('', safe=False)
    if request.is_ajax():
        icd_10_codes = Icd10Codes.objects.filter(id__in=ids)
        response_text = ''
        for icd_10_code in icd_10_codes:
            if icd_10_code.abbreviated_description:
                response_text += icd_10_code.full_code + ': ' + icd_10_code.abbreviated_description + ' '
        return JsonResponse(response_text, safe=False)
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
