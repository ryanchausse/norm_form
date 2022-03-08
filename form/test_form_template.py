from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.colors import white
from reportlab.platypus import paragraph
import datetime
import os

filename = 'sample_form_template.pdf'
pdf = canvas.Canvas(filename=os.path.abspath(os.path.dirname(__file__)) + '/templates/forms/' + filename,
                    pagesize=letter)
width, height = letter
# Width = 612(px?), Height = 792
pdf.setLineWidth(.3)
pdf.setTitle(filename)
doc_title_text = 'Psychologist Consultation / Follow-Up'
doc_title_text_width = stringWidth(doc_title_text, 'Helvetica-Bold', 20)
pdf.setFont('Helvetica', 20)
pdf.drawString((width-doc_title_text_width)/2, 760, doc_title_text)

# Intro demographic info and Subjective section
pdf.setFont('Helvetica', 10)
pdf.drawString(30, 730, 'Patient Name:')
pdf.drawString(280, 730, 'Facility:')
pdf.drawString(480, 730, 'Date:')
pdf.setFont('Helvetica-Bold', 10)
pdf.drawString(30, 710, 'Subjective (Chief Complaints, Presenting Problems, and History):')

# Title for Mental Status Exam (Objective section)
mental_status_text = 'Mental Status Examination'
mental_status_text_width = stringWidth(mental_status_text, 'Helvetica', 14)
pdf.setFont('Helvetica', 14)
pdf.drawString((width-mental_status_text_width)/2, 635, mental_status_text)

# Fields for Objective section
# Can also use acroforms for interactive form fields like checkboxes
# e.g. pdf.acroForm.checkbox(x=95, y=547, size=13, fillColor=white, checked=True)
pdf.setFont('Helvetica-Bold', 10)
pdf.drawString(30, 615, 'Objective (Staff/Other Sources Reported):')

# Aggressive Behavior
pdf.setFont('Helvetica', 10)
pdf.drawString(30, 600, 'Aggressive Behavior:')
pdf.drawString(42, 585, 'Physical')
pdf.rect(x=85, y=585, width=10, height=10)
if 'form to save.physical':
    pdf.drawString(86, 586, '✔')
pdf.drawString(115, 585, 'Verbal')
pdf.rect(x=149, y=585, width=10, height=10)
if 'form to save.verbal':
    pdf.drawString(150, 586, '✔')
pdf.drawString(170, 585, 'Gestures')
pdf.rect(x=216, y=585, width=10, height=10)
if 'form to save.gestures':
    pdf.drawString(217, 586, '✔')
pdf.drawString(235, 585, 'Threatening Behaviors')
pdf.rect(x=342, y=585, width=10, height=10)
if 'form to save.threatening_behaviors':
    pdf.drawString(343, 586, '✔')
pdf.drawString(360, 585, '<<Aggressive behavior notes here>>')

# General Appearance
pdf.setFont('Helvetica', 10)
pdf.drawString(30, 570, 'General Appearance:')
pdf.drawString(42, 557, 'Well Groomed')
pdf.rect(x=110, y=557, width=10, height=10)
if 'form to save.well_groomed':
    pdf.drawString(111, 558, '✔')
pdf.drawString(130, 557, 'Fairly Groomed')
pdf.rect(x=201, y=557, width=10, height=10)
if 'form to save.fairly_groomed':
    pdf.drawString(202, 558, '✔')
pdf.drawString(228, 557, 'Poorly Groomed')
pdf.rect(x=305, y=557, width=10, height=10)
if 'form to save.poorly_groomed':
    pdf.drawString(306, 558, '✔')
pdf.drawString(330, 557, 'Disheveled')
pdf.rect(x=383, y=557, width=10, height=10)
if 'form to save.disheveled':
    pdf.drawString(384, 558, '✔')
pdf.drawString(400, 557, '<<General appearance notes here>>')

# Treatment and Compliance
pdf.setFont('Helvetica', 10)
pdf.drawString(30, 570, 'General Appearance:')
pdf.drawString(42, 557, 'Well Groomed')
pdf.rect(x=110, y=557, width=10, height=10)
if 'form to save.well_groomed':
    pdf.drawString(111, 558, '✔')
pdf.drawString(130, 557, 'Fairly Groomed')
pdf.rect(x=201, y=557, width=10, height=10)
if 'form to save.fairly_groomed':
    pdf.drawString(202, 558, '✔')
pdf.drawString(228, 557, 'Poorly Groomed')
pdf.rect(x=305, y=557, width=10, height=10)
if 'form to save.poorly_groomed':
    pdf.drawString(306, 558, '✔')
pdf.drawString(330, 557, 'Disheveled')
pdf.rect(x=383, y=557, width=10, height=10)
if 'form to save.disheveled':
    pdf.drawString(384, 558, '✔')
pdf.drawString(400, 557, '<<General appearance notes here>>')


pdf.setFont('Helvetica', 8)
pdf.drawString(5, 5, f'Date: {str(datetime.date.today())} Patient: SampleFirst SampleLast'
                     f'Facility: Sample Hospital Time printed: {str(datetime.datetime.now())}')
pdf.showPage()
pdf.save()
