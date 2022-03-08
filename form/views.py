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
from reportlab.pdfbase.pdfmetrics import stringWidth
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
            # Width = 612(px?), Height = 792
            pdf.setLineWidth(.3)
            pdf.setTitle(filename)
            doc_title_text = 'Psychologist Consultation / Follow-Up'
            doc_title_text_width = stringWidth(doc_title_text, 'Helvetica-Bold', 20)
            pdf.setFont('Helvetica', 20)
            pdf.drawString((width - doc_title_text_width) / 2, 760, doc_title_text)

            # Intro demographic info and Subjective section
            pdf.setFont('Helvetica', 10)
            pdf.drawString(30, 730, 'Patient Name:')
            pdf.drawString(280, 730, 'Facility:')
            pdf.drawString(480, 730, 'Date:')
            pdf.setFont('Helvetica-Bold', 10)
            pdf.drawString(30, 710, 'Subjective (Chief Complaints, Presenting Problems, and History):')
            if form_to_save.chief_complaints_problems_history:
                pdf.setFont('Helvetica', 10)
                pdf.drawString(40, 690, form_to_save.chief_complaints_problems_history)

            # Title for Mental Status Exam (Objective section)
            mental_status_text = 'Mental Status Examination'
            mental_status_text_width = stringWidth(mental_status_text, 'Helvetica', 14)
            pdf.setFont('Helvetica', 14)
            pdf.drawString((width - mental_status_text_width) / 2, 635, mental_status_text)

            # Fields for Objective section
            # Can also use acroforms for interactive form fields like checkboxes
            # e.g. pdf.acroForm.checkbox(x=95, y=547, size=13, fillColor=white, checked=True)
            pdf.setFont('Helvetica-Bold', 10)
            pdf.drawString(30, 617, 'Objective (Staff/Other Sources Reported):')

            #
            # Aggressive Behavior
            #
            pdf.setFont('Helvetica', 8)
            pdf.drawString(30, 600, 'Aggressive Behavior:')

            # Physical
            pdf.rect(x=140, y=600, width=10, height=10)
            if form_to_save.agg_behavior_physical:
                pdf.drawString(142, 602, '✔')
            pdf.drawString(155, 600, 'Physical')

            # Verbal
            pdf.rect(x=200, y=600, width=10, height=10)
            if form_to_save.agg_behavior_verbal:
                pdf.drawString(202, 602, '✔')
            pdf.drawString(215, 600, 'Verbal')

            # Gestures
            pdf.rect(x=255, y=600, width=10, height=10)
            if form_to_save.agg_behavior_gestures:
                pdf.drawString(257, 602, '✔')
            pdf.drawString(270, 600, 'Gestures')

            # Threatening Behaviors
            pdf.rect(x=312, y=600, width=10, height=10)
            if form_to_save.agg_behavior_threatening:
                pdf.drawString(314, 602, '✔')
            pdf.drawString(327, 600, 'Threatening Behaviors')

            # Aggressive behavior notes
            # pdf.drawString(412, 600, '<<Aggressive behavior notes here>>')

            #
            # General appearance
            #
            pdf.setFont('Helvetica', 8)
            pdf.drawString(30, 580, 'General Appearance:')

            # Well groomed
            pdf.rect(x=140, y=580, width=10, height=10)
            if form_to_save.gen_appearance_well_groomed:
                pdf.drawString(142, 582, '✔')
            pdf.drawString(155, 580, 'Well Groomed')

            # Fairly groomed
            pdf.rect(x=215, y=580, width=10, height=10)
            if form_to_save.gen_appearance_fairly_groomed:
                pdf.drawString(217, 582, '✔')
            pdf.drawString(229, 580, 'Fairly groomed')

            # Poorly groomed
            pdf.rect(x=289, y=580, width=10, height=10)
            if form_to_save.gen_appearance_poorly_groomed:
                pdf.drawString(291, 582, '✔')
            pdf.drawString(301, 580, 'Poorly groomed')

            # Disheveled
            pdf.rect(x=365, y=580, width=10, height=10)
            if form_to_save.gen_appearance_disheveled:
                pdf.drawString(367, 582, '✔')
            pdf.drawString(379, 580, 'Disheveled')

            # General Appearance notes
            # pdf.drawString(422, 580, '<<General appearance notes here>>')

            #
            # Treatment & Compliance
            #
            pdf.setFont('Helvetica', 8)
            pdf.drawString(30, 560, 'Treatment & Compliance:')

            # Acceptable
            pdf.rect(x=140, y=560, width=10, height=10)
            if form_to_save.treat_and_compliance_acceptable:
                pdf.drawString(142, 562, '✔')
            pdf.drawString(155, 560, 'Acceptable')

            # Low Motivation
            pdf.rect(x=205, y=560, width=10, height=10)
            if form_to_save.treat_and_compliance_low_motivation:
                pdf.drawString(207, 562, '✔')
            pdf.drawString(219, 560, 'Low Motivation')

            # Resistive
            pdf.rect(x=282, y=560, width=10, height=10)
            if form_to_save.treat_and_compliance_resistive:
                pdf.drawString(284, 562, '✔')
            pdf.drawString(294, 560, 'Resistive')

            # Argumentative
            pdf.rect(x=337, y=560, width=10, height=10)
            if form_to_save.treat_and_compliance_argumentative:
                pdf.drawString(339, 562, '✔')
            pdf.drawString(351, 560, 'Argumentative')

            # Exit seeking
            pdf.rect(x=409, y=560, width=10, height=10)
            if form_to_save.treat_and_compliance_exit_seeking:
                pdf.drawString(411, 562, '✔')
            pdf.drawString(423, 560, 'Exit Seeking')

            # Treatment & Compliance notes
            # pdf.drawString(469, 560, '<<Treatment & Compliance notes here>>')

            #
            # Inappropriate Behavior
            #
            pdf.setFont('Helvetica', 8)
            pdf.drawString(30, 540, 'Inappropriate Behavior:')

            # Inappropriate Behavior
            pdf.rect(x=140, y=540, width=10, height=10)
            if form_to_save.inappropriate_behavior:
                pdf.drawString(142, 542, '✔')
            pdf.drawString(155, 540, 'Inappropriate Behavior')

            # Inappropriate Behavior notes
            # pdf.drawString(245, 540, '<<Inappropriate Behavior notes here>>')

            #
            # Attitude
            #
            pdf.setFont('Helvetica', 8)
            pdf.drawString(30, 520, 'Attitude:')

            # Cooperative
            pdf.rect(x=140, y=520, width=10, height=10)
            if form_to_save.attitude_cooperative:
                pdf.drawString(142, 522, '✔')
            pdf.drawString(155, 520, 'Cooperative')

            # Uncooperative
            pdf.rect(x=205, y=520, width=10, height=10)
            if form_to_save.attitude_uncooperative:
                pdf.drawString(207, 522, '✔')
            pdf.drawString(219, 520, 'Uncooperative')

            # Marginally Cooperative
            pdf.rect(x=278, y=520, width=10, height=10)
            if form_to_save.attitude_marginally_cooperative:
                pdf.drawString(280, 522, '✔')
            pdf.drawString(292, 520, 'Marginally Cooperative')

            # Attitude - other
            pdf.rect(x=383, y=520, width=10, height=10)
            if form_to_save.attitude_other:
                pdf.drawString(385, 522, '✔')
            pdf.drawString(395, 520, 'Other')

            # Attitude notes
            # pdf.drawString(424, 520, '<<Attitude notes here>>')

            #
            # Speech
            #
            pdf.setFont('Helvetica', 8)
            pdf.drawString(30, 500, 'Speech:')

            # Intact
            pdf.rect(x=140, y=500, width=10, height=10)
            if form_to_save.speech_intact:
                pdf.drawString(142, 502, '✔')
            pdf.drawString(155, 500, 'Intact')

            # Pressured
            pdf.rect(x=185, y=500, width=10, height=10)
            if form_to_save.speech_pressured:
                pdf.drawString(187, 502, '✔')
            pdf.drawString(198, 500, 'Pressured')

            # Hyperverbal
            pdf.rect(x=244, y=500, width=10, height=10)
            if form_to_save.speech_hyperverbal:
                pdf.drawString(246, 502, '✔')
            pdf.drawString(257, 500, 'Hyperverbal')

            # Loud
            pdf.rect(x=310, y=500, width=10, height=10)
            if form_to_save.speech_loud:
                pdf.drawString(312, 502, '✔')
            pdf.drawString(323, 500, 'Loud')

            # Slow
            pdf.rect(x=350, y=500, width=10, height=10)
            if form_to_save.speech_slow:
                pdf.drawString(352, 502, '✔')
            pdf.drawString(363, 500, 'Slow')

            # Unintelligible
            pdf.rect(x=385, y=500, width=10, height=10)
            if form_to_save.speech_unintelligible:
                pdf.drawString(387, 502, '✔')
            pdf.drawString(400, 500, 'Unintelligible')

            # Yelling Out
            pdf.rect(x=140, y=480, width=10, height=10)
            if form_to_save.speech_yelling_out:
                pdf.drawString(142, 482, '✔')
            pdf.drawString(155, 480, 'Yelling Out')

            # Perseverative
            pdf.rect(x=204, y=480, width=10, height=10)
            if form_to_save.speech_perseverative:
                pdf.drawString(206, 482, '✔')
            pdf.drawString(218, 480, 'Perseverative')

            # Speech notes
            # pdf.drawString(275, 480, '<<Speech notes here>>')

            #
            # Verbal Abilities
            #
            pdf.setFont('Helvetica', 8)
            pdf.drawString(30, 460, 'Verbal Abilities:')

            # Receptive language
            pdf.setFont('Helvetica-Bold', 8)
            pdf.drawString(140, 462, 'Receptive Language:')
            pdf.setFont('Helvetica', 8)
            pdf.rect(x=230, y=460, width=10, height=10)
            if form_to_save.verbal_abilities_receptive_language_sufficient:
                pdf.drawString(232, 462, '✔')
            pdf.drawString(245, 462, 'Sufficient')
            pdf.rect(x=288, y=460, width=10, height=10)
            if form_to_save.verbal_abilities_receptive_language_impaired:
                pdf.drawString(290, 462, '✔')
            pdf.drawString(300, 462, 'Impaired')

            # Expressive language
            pdf.setFont('Helvetica-Bold', 8)
            pdf.drawString(340, 462, 'Expressive Language:')
            pdf.setFont('Helvetica', 8)
            pdf.rect(x=433, y=460, width=10, height=10)
            if form_to_save.verbal_abilities_expressive_language_sufficient:
                pdf.drawString(435, 462, '✔')
            pdf.drawString(447, 462, 'Sufficient')
            pdf.rect(x=486, y=460, width=10, height=10)
            if form_to_save.verbal_abilities_expressive_language_impaired:
                pdf.drawString(488, 462, '✔')
            pdf.drawString(500, 462, 'Impaired')

            # Verbal Abilities notes
            # pdf.drawString(550, 460, '<<Verbal Abilities notes here>>')

            pdf.setFont('Helvetica', 8)
            pdf.drawString(5, 5, f'Date: {str(datetime.date.today())} Patient: SampleFirst SampleLast'
                                 f'Facility: Sample Hospital Time printed: {str(datetime.datetime.now())}')
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
