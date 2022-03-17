# Sample platypus document
# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT


width, height = letter
# Width = 612(px?), Height = 792

pageinfo = "Dr. Hendricksen evaluation form"


class InteractiveCheckBox(Flowable):
    def __init__(self, name, tooltip="", checked=False, size=12, button_style="check"):
        Flowable.__init__(self)
        self.name = name
        self.tooltip = tooltip
        self.size = size
        self.checked = checked
        self.buttonStyle = button_style

    def draw(self):
        self.canv.saveState()
        form = self.canv.acroForm
        form.checkbox(checked=self.checked,
                      buttonStyle=self.buttonStyle,
                      name=self.name,
                      tooltip=self.tooltip,
                      relative=True,
                      size=self.size)
        self.canv.restoreState()


def first_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.restoreState()


def build_form():
    doc = SimpleDocTemplate("templates/forms/flowable_test.pdf", rightMargin=15, leftMargin=15,
                            topMargin=10, bottomMargin=10)
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

    # Checkbox fields
    # p = Paragraph(f'Aggressive Behavior:',
    #               style=ParagraphStyle(name='Normal', fontName='Helvetica',
    #                                    fontSize=9, alignment=TA_LEFT))
    # story.append(p)

    data = [['Aggressive Behavior',
             'Physical:', InteractiveCheckBox("physical", "Physical"),
             'Verbal:', InteractiveCheckBox("verbal", "Verbal"),
             'Gestures:', InteractiveCheckBox("Gestures", "Gestures"),
             'Threatening Behaviors:', InteractiveCheckBox("threatening_behaviors", "Threatening Behaviors"),
             ]]
    grid = [
        ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('ALIGN', (2, 0), (2, 0), 'LEFT'),
        ('ALIGN', (3, 0), (3, 0), 'RIGHT'),
        ('ALIGN', (4, 0), (4, 0), 'LEFT'),
        ('ALIGN', (5, 0), (5, 0), 'RIGHT'),
        ('ALIGN', (6, 0), (6, 0), 'LEFT'),
        ('ALIGN', (7, 0), (7, 0), 'RIGHT'),
        ('ALIGN', (8, 0), (8, 0), 'LEFT'),
        ('ALIGN', (9, 0), (9, 0), 'RIGHT'),
        ('ALIGN', (10, 0), (10, 0), 'LEFT'),
        ('ALIGN', (11, 0), (11, 0), 'RIGHT'),
        ('ALIGN', (12, 0), (12, 0), 'LEFT'),
        ('ALIGN', (13, 0), (13, 0), 'RIGHT'),
        ('ALIGN', (14, 0), (14, 0), 'LEFT'),
        ('ALIGN', (15, 0), (15, 0), 'RIGHT'),
        ('ALIGN', (16, 0), (16, 0), 'LEFT'),
        ('ALIGN', (17, 0), (17, 0), 'RIGHT'),
        ('ALIGN', (18, 0), (18, 0), 'LEFT'),
    ]
    t = Table(data, style=TableStyle(grid))
    story.append(t)

    doc.build(story, onFirstPage=first_page)


if __name__ == "__main__":
    build_form()
