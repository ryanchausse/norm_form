# Sample platypus document
# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Flowable, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import BaseDocTemplate, PageBreak, FrameBreak, Frame
from reportlab.pdfgen import canvas
from reportlab.platypus import flowables
from reportlab.graphics.shapes import Rect
from reportlab.graphics.shapes import Drawing


width, height = letter
# Width = 612(px?), Height = 792

pageinfo = "Dr. Hendricksen evaluation form"


class UncheckedBox(Flowable):
    def __init__(self, width=10, height=10):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        self.canv.rect(0, 2, self.width, self.height, fill=0)


class CheckedBox(Flowable):
    def __init__(self, width=10, height=10):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        self.canv.rect(0, 2, self.width, self.height, fill=0)
        self.canv.drawCentredString(0.5 * self.width, 0.5 * self.height, '✓')


class NormFormDocTemplate(BaseDocTemplate):
    def build(self, flowables):
        self._calc()
        print(self.height)  # 821.89
        print(self.width)  # 565.28
        frame_top = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id='frame_top')
        frame_left = Frame(self.leftMargin, -158, 115, self.height, id='frame_left')
        frame_right = Frame(self.leftMargin + 110, -155, 450, self.height, id='frame_right')
        self.addPageTemplates([PageTemplate(id='First', frames=[frame_top, frame_left, frame_right], pagesize=self.pagesize)])
        BaseDocTemplate.build(self, flowables)


def build_form():
    doc = NormFormDocTemplate("templates/forms/flowable_test.pdf", rightMargin=15, leftMargin=15,
                              topMargin=10, bottomMargin=10)
    # doc = SimpleDocTemplate("templates/forms/flowable_test.pdf", rightMargin=15, leftMargin=15,
    #                         topMargin=10, bottomMargin=10)
    story = []
    title_text = "Psychologist Consultation / Follow-Up"
    p = Paragraph(title_text, style=ParagraphStyle(name='Normal', fontName='Helvetica', fontSize=12,
                                                   alignment=TA_CENTER))
    story.append(p)

    story.append(Spacer(0, 0.1*inch))

    data = [['Patient Name', 'Facility', 'Date'],
            ['Lastname, Firstname', 'TestFacility', '01/01/1950']]
    grid = [('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]
    t = Table(data, colWidths=[3.95*inch, 2.95*inch, 0.95*inch], hAlign=TA_LEFT, style=TableStyle(grid))
    story.append(t)

    story.append(Spacer(0, 0.1 * inch))

    p = Paragraph(f'Subjective (Chief Complaints, Presenting Problems, and History):',
                  style=ParagraphStyle(name='Normal', fontName='Helvetica-Bold',
                                       fontSize=9, alignment=TA_LEFT))
    story.append(p)
    p = Paragraph(f'Insert eval here',
                  style=ParagraphStyle(name='Normal', leftIndent=10, fontName='Helvetica',
                                       fontSize=9, alignment=TA_LEFT))
    story.append(p)

    story.append(Spacer(0, 0.7 * inch))

    p = Paragraph(f'Mental Status Examination',
                  style=ParagraphStyle(name='Normal', fontName='Helvetica',
                                       fontSize=12, alignment=TA_CENTER))
    story.append(p)
    p = Paragraph(f'Objective (Staff / Other Sources Reported)',
                  style=ParagraphStyle(name='Normal', fontName='Helvetica-Bold',
                                       fontSize=9, alignment=TA_LEFT))
    story.append(p)

    story.append(Spacer(0, 0.1 * inch))

    story.append(FrameBreak)

    p = Paragraph('Aggressive Behavior<br /><br />'
                  'General Appearance<br /><br />'
                  'Treatment & Compliance<br /><br />'
                  'Inappropriate Behavior<br /><br />'
                  'Attitude<br /><br />'
                  'Speech<br /><br />'
                  'Verbal Abilities<br /><br />'
                  'Communication<br /><br />'
                  'Perceptual Disturbances<br /><br />'
                  'Level of Consciousness<br /><br />'
                  'Thought Process<br /><br />'
                  'Thought Content<br /><br />'
                  'Mood<br /><br />'
                  'Affect<br /><br />'
                  'Harmfulness<br /><br />'
                  'Attention & Concentration<br /><br />'
                  'Orientation<br /><br />'
                  'Insight & Judgment<br /><br />'
                  'Sleep Disturbance<br /><br />'
                  'Appetite change',
                  style=ParagraphStyle(name='Normal', fontName='Helvetica',
                                       fontSize=8, alignment=TA_RIGHT))
    story.append(p)

    story.append(FrameBreak)

    grid = [
        ('FONTNAME', (1, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (0, 0), 'RIGHT'),
        ('ALIGN', (1, 0), (1, 0), 'LEFT'),
        ('RIGHTPADDING', (0, 0), (0, 0), 2),
        ('LEFTPADDING', (1, 0), (1, 0), 2),
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
        ('ALIGN', (3, 0), (3, 0), 'LEFT'),
        ('RIGHTPADDING', (2, 0), (2, 0), 2),
        ('LEFTPADDING', (3, 0), (3, 0), 2),
        ('ALIGN', (4, 0), (4, 0), 'RIGHT'),
        ('ALIGN', (5, 0), (5, 0), 'LEFT'),
        ('RIGHTPADDING', (4, 0), (4, 0), 2),
        ('LEFTPADDING', (5, 0), (5, 0), 2),
        ('ALIGN', (6, 0), (6, 0), 'RIGHT'),
        ('ALIGN', (7, 0), (7, 0), 'LEFT'),
        ('RIGHTPADDING', (6, 0), (6, 0), 2),
        ('LEFTPADDING', (7, 0), (7, 0), 2),
        ('ALIGN', (8, 0), (8, 0), 'RIGHT'),
        ('ALIGN', (9, 0), (9, 0), 'LEFT'),
        ('RIGHTPADDING', (8, 0), (8, 0), 2),
        ('LEFTPADDING', (9, 0), (9, 0), 2),
        ('ALIGN', (10, 0), (10, 0), 'RIGHT'),
        ('ALIGN', (11, 0), (11, 0), 'LEFT'),
        ('RIGHTPADDING', (10, 0), (10, 0), 2),
        ('LEFTPADDING', (11, 0), (11, 0), 2),
        ('ALIGN', (12, 0), (12, 0), 'RIGHT'),
        ('ALIGN', (13, 0), (13, 0), 'LEFT'),
        ('RIGHTPADDING', (12, 0), (12, 0), 2),
        ('LEFTPADDING', (13, 0), (13, 0), 2),
        ('ALIGN', (14, 0), (14, 0), 'RIGHT'),
        ('ALIGN', (15, 0), (15, 0), 'LEFT'),
        ('RIGHTPADDING', (14, 0), (14, 0), 2),
        ('LEFTPADDING', (15, 0), (15, 0), 2),
        ('ALIGN', (16, 0), (16, 0), 'RIGHT'),
        ('ALIGN', (17, 0), (17, 0), 'LEFT'),
        ('RIGHTPADDING', (16, 0), (16, 0), 2),
        ('LEFTPADDING', (17, 0), (17, 0), 2),
        ('ALIGN', (18, 0), (18, 0), 'RIGHT'),
        ('ALIGN', (19, 0), (19, 0), 'LEFT'),
        ('RIGHTPADDING', (18, 0), (18, 0), 2),
        ('LEFTPADDING', (19, 0), (19, 0), 2),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 8.9)
    ]

    data = [[# 'Aggressive Behavior:',
        # Eventually, do CheckedBox() if {{ physical }} else UncheckedBox
            'Physical', CheckedBox(),
            'Verbal', UncheckedBox(),
            'Gestures', UncheckedBox(),
            'Threatening Behaviors', UncheckedBox()
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=None)
    story.append(t)

    # Separate tables needed for formatting / length overruns on vertically justified columns
    data = [[# 'General Appearance:',
             'Well Groomed', CheckedBox(),
             'Fairly Groomed', UncheckedBox(),
             'Poorly Groomed', UncheckedBox(),
             'Disheveled', UncheckedBox()
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=None)
    story.append(t)

    data = [[# 'Treatment & Compliance:',
             'Acceptable', CheckedBox(),
             'Low Motivation', UncheckedBox(),
             'Resistive', UncheckedBox(),
             'Argumentative', UncheckedBox(),
             'Exit Seeking', UncheckedBox(),
             'Wandering', UncheckedBox()
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=None)
    story.append(t)

    data = [[# 'Inappropriate Behavior:',
             'Inappropriate Behavior', UncheckedBox(),
             'Describe:', ' ', ' ', ' ', ' ']]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=None)
    story.append(t)

    # doc.build(story, onFirstPage=first_page)
    doc.build(story)


if __name__ == "__main__":
    build_form()
