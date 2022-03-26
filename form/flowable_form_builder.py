from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Flowable, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import BaseDocTemplate, PageBreak, FrameBreak, Frame

width, height = letter
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
        frame_left = Frame(self.leftMargin, -125, 115, self.height, id='frame_left')
        frame_right = Frame(self.leftMargin + 110, -123, 450, self.height, id='frame_right')
        frame_bottom = Frame(self.leftMargin, self.bottomMargin, 7 * inch, 3 * inch, id='frame_bottom')
        self.addPageTemplates([PageTemplate(id='First', frames=[frame_top, frame_left, frame_right, frame_bottom],
                                            pagesize=self.pagesize)])
        BaseDocTemplate.build(self, flowables)


def build_form(form_to_save=None, filename=None):
    if not form_to_save or not filename:
        raise ValueError('Form or filename has not been supplied')
    doc = NormFormDocTemplate(filename, rightMargin=15, leftMargin=15,
                              topMargin=10, bottomMargin=10, title=form_to_save.filename)
    # doc = SimpleDocTemplate("templates/forms/flowable_test.pdf", rightMargin=15, leftMargin=15,
    #                         topMargin=10, bottomMargin=10)
    story = []
    title_text = "Psychologist Consultation / Follow-Up"
    p = Paragraph(title_text, style=ParagraphStyle(name='Normal', fontName='Helvetica', fontSize=12,
                                                   alignment=TA_CENTER))
    story.append(p)

    story.append(Spacer(0, 0.1*inch))

    data = [['Patient Name',
             'Facility',
             'Date'],
            [f'{form_to_save.patient.last_name}, {form_to_save.patient.first_name}',
             f'{form_to_save.facility.name}',
             f'{form_to_save.date}']]
    grid = [('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]
    t = Table(data, colWidths=[3.95*inch, 2.95*inch, 0.95*inch], hAlign=TA_LEFT, style=TableStyle(grid))
    story.append(t)

    story.append(Spacer(0, 0.1 * inch))

    p = Paragraph(f'Subjective (Chief Complaints, Presenting Problems, and History):',
                  style=ParagraphStyle(name='Normal', fontName='Helvetica-Bold',
                                       fontSize=9, alignment=TA_LEFT))
    story.append(p)

    if form_to_save.chief_complaints_problems_history:
        p = Paragraph(f'{form_to_save.chief_complaints_problems_history}',
                      style=ParagraphStyle(name='Normal', leftIndent=10, fontName='Helvetica',
                                           fontSize=9, alignment=TA_LEFT))
        story.append(p)

    story.append(Spacer(0, 0.3 * inch))

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
                  style=ParagraphStyle(name='Normal', fontName='Helvetica-Bold',
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
            'Physical', CheckedBox() if form_to_save.agg_behavior_physical else UncheckedBox(),
            'Verbal', CheckedBox() if form_to_save.agg_behavior_verbal else UncheckedBox(),
            'Gestures', CheckedBox() if form_to_save.agg_behavior_gestures else UncheckedBox(),
            'Threatening Behaviors', CheckedBox() if form_to_save.agg_behavior_threatening else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, 2.5*inch])
    story.append(t)

    # Separate tables needed for formatting / length overruns on vertically justified columns
    data = [[# 'General Appearance:',
             'Well Groomed', CheckedBox() if form_to_save.gen_appearance_well_groomed else UncheckedBox(),
             'Fairly Groomed', CheckedBox() if form_to_save.gen_appearance_fairly_groomed else UncheckedBox(),
             'Poorly Groomed', CheckedBox() if form_to_save.gen_appearance_poorly_groomed else UncheckedBox(),
             'Disheveled', CheckedBox() if form_to_save.gen_appearance_disheveled else UncheckedBox()
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, 2*inch])
    story.append(t)

    data = [[# 'Treatment & Compliance:',
             'Acceptable', CheckedBox() if form_to_save.treat_and_compliance_acceptable else UncheckedBox(),
             'Low Motivation', CheckedBox() if form_to_save.treat_and_compliance_low_motivation else UncheckedBox(),
             'Resistive', CheckedBox() if form_to_save.treat_and_compliance_resistive else UncheckedBox(),
             'Argumentative', CheckedBox() if form_to_save.treat_and_compliance_argumentative else UncheckedBox(),
             'Exit Seeking', CheckedBox() if form_to_save.treat_and_compliance_exit_seeking else UncheckedBox(),
             'Wandering', CheckedBox() if form_to_save.agg_behavior_physical else UncheckedBox()
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, None,
                                                                       None, None, None, 0.5*inch])
    story.append(t)

    data = [[# 'Inappropriate Behavior:',
            'Inappropriate Behavior', CheckedBox() if form_to_save.inappropriate_behavior else UncheckedBox(),
            'Describe:', f'test describe text'
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, 4*inch])
    story.append(t)

    data = [[# 'Attitude:',
             'Cooperative', CheckedBox() if form_to_save.attitude_cooperative else UncheckedBox(),
             'Uncooperative', CheckedBox() if form_to_save.attitude_uncooperative else UncheckedBox(),
             'Marginally Cooperative', CheckedBox() if form_to_save.attitude_marginally_cooperative else UncheckedBox(),
             'Describe:', 'test describe text'
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, 2*inch])
    story.append(t)

    data = [[# 'Speech:',
        'Intact', CheckedBox() if form_to_save.speech_intact else UncheckedBox(),
        'Pressured', CheckedBox() if form_to_save.speech_pressured else UncheckedBox(),
        'Hyperverbal', CheckedBox() if form_to_save.speech_hyperverbal else UncheckedBox(),
        'Loud', CheckedBox() if form_to_save.speech_loud else UncheckedBox(),
        'Slow', CheckedBox() if form_to_save.speech_slow else UncheckedBox(),
        'Yelling Out', CheckedBox() if form_to_save.speech_yelling_out else UncheckedBox(),
        'Perseverative', CheckedBox() if form_to_save.speech_perseverative else UncheckedBox()
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT)
    story.append(t)

    data = [[# 'Verbal Abilities:',
        Paragraph('Receptive Language:', style=ParagraphStyle(name='Normal', fontName='Helvetica-Bold',
                                       fontSize=8, alignment=TA_RIGHT)),
        '',
        'Sufficient', CheckedBox() if form_to_save.verbal_abilities_receptive_language_sufficient else UncheckedBox(),
        'Impaired', CheckedBox() if form_to_save.verbal_abilities_receptive_language_impaired else UncheckedBox(),
        Paragraph('Expressive Language:', style=ParagraphStyle(name='Normal', fontName='Helvetica-Bold',
                                       fontSize=8, alignment=TA_RIGHT)),
        '',
        'Sufficient', CheckedBox() if form_to_save.verbal_abilities_expressive_language_sufficient else UncheckedBox(),
        'Impaired', CheckedBox() if form_to_save.verbal_abilities_expressive_language_impaired else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT,
              colWidths=[1.5*inch, 0.01*inch, None, None,
                         None, None, 1.5*inch, 0.01*inch,
                         None, None, None, 0.65*inch]
              )
    story.append(t)

    data = [[# 'Communication:',
        'Verbal', CheckedBox() if form_to_save.communication_verbal else UncheckedBox(),
        'Non-verbal', CheckedBox() if form_to_save.communication_non_verbal else UncheckedBox(),
        'Minimally Verbal', CheckedBox() if form_to_save.communication_minimally_verbal else UncheckedBox(),
        'Withdrawn', CheckedBox() if form_to_save.communication_withdrawn else UncheckedBox(),
        'Avoidant', CheckedBox() if form_to_save.communication_avoidant else UncheckedBox(),
        'Evasive', CheckedBox() if form_to_save.communication_evasive else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, None,
                                                                       None, None, None, inch])
    story.append(t)

    data = [[# 'Perceptual Disturbances:',
        'None', CheckedBox() if form_to_save.perceptual_disturbances_none else UncheckedBox(),
        'Hallucinations', CheckedBox() if form_to_save.perceptual_disturbances_hallucinations else UncheckedBox(),
        'Visual', CheckedBox() if form_to_save.perceptual_disturbances_visual else UncheckedBox(),
        'Auditory', CheckedBox() if form_to_save.perceptual_disturbances_auditory else UncheckedBox(),
        'Command', CheckedBox() if form_to_save.perceptual_disturbances_command else UncheckedBox(),
        'Tactile', CheckedBox() if form_to_save.perceptual_disturbances_tactile else UncheckedBox(),
        'Olfactory', CheckedBox() if form_to_save.perceptual_disturbances_olfactory else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, None,
                                                                       None, None, None, None,
                                                                       None, 0.5*inch])
    story.append(t)

    data = [[# 'Level of Consciousness:',
        'Alert', CheckedBox() if form_to_save.level_of_consciousness_alert else UncheckedBox(),
        'Confused', CheckedBox() if form_to_save.level_of_consciousness_confused else UncheckedBox(),
        'Drowsy', CheckedBox() if form_to_save.level_of_consciousness_drowsy else UncheckedBox(),
        'Somnolent', CheckedBox() if form_to_save.level_of_consciousness_somnolent else UncheckedBox(),
        'Fluctuating', CheckedBox() if form_to_save.level_of_consciousness_fluctuating else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, None,
                                                                       None, 2*inch])
    story.append(t)

    data = [[# 'Thought Process:',
        'Linear', CheckedBox() if form_to_save.thought_process_linear else UncheckedBox(),
        'Disorganized', CheckedBox() if form_to_save.thought_process_disorganized else UncheckedBox(),
        'Fragmented', CheckedBox() if form_to_save.thought_process_fragmented else UncheckedBox(),
        'Racing', CheckedBox() if form_to_save.thought_process_racing else UncheckedBox(),
        'Circumstantial', CheckedBox() if form_to_save.thought_process_circumstantial else UncheckedBox(),
        'Tangential', CheckedBox() if form_to_save.thought_process_tangential else UncheckedBox(),
        'Blocking', CheckedBox() if form_to_save.thought_process_blocking else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, None,
                                                                       None, None, None, None,
                                                                       None, 0.1 * inch])
    story.append(t)

    data = [[# 'Thought Content:',
        'Normal', CheckedBox() if form_to_save.thought_content_normal else UncheckedBox(),
        'Delusions', CheckedBox() if form_to_save.thought_content_delusions else UncheckedBox(),
        'Persecutory', CheckedBox() if form_to_save.thought_content_persecutory else UncheckedBox(),
        'Grandiose', CheckedBox() if form_to_save.thought_content_grandiose else UncheckedBox(),
        'Religious', CheckedBox() if form_to_save.thought_content_religious else UncheckedBox(),
        'Self-Referential', CheckedBox() if form_to_save.thought_content_self_referential else UncheckedBox(),
        'Poverty of Content', CheckedBox() if form_to_save.thought_content_poverty_of_content else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, 0.17 * inch, None, 0.17 * inch,
                                                                       None, 0.17 * inch, None, 0.17 * inch,
                                                                       None, 0.17 * inch, None, 0.17 * inch,
                                                                       None, 0.19 * inch])
    story.append(t)

    data = [[# 'Mood:',
        'Euthymic', CheckedBox() if form_to_save.mood_euthymic else UncheckedBox(),
        'Depressed', CheckedBox() if form_to_save.mood_depressed else UncheckedBox(),
        'Anxious', CheckedBox() if form_to_save.mood_anxious else UncheckedBox(),
        'Irritable', CheckedBox() if form_to_save.mood_irritable else UncheckedBox(),
        'Angry', CheckedBox() if form_to_save.mood_angry else UncheckedBox(),
        'Tearful', CheckedBox() if form_to_save.mood_tearful else UncheckedBox(),
        'Elated', CheckedBox() if form_to_save.mood_elated else UncheckedBox(),
        'Labile', CheckedBox() if form_to_save.mood_labile else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, None,
                                                                       None, None, None, None,
                                                                       None, None, None, 0.25 * inch])
    story.append(t)

    data = [[# 'Affect:',
        'Appropriate', CheckedBox() if form_to_save.affect_appropriate else UncheckedBox(),
        'Flat', CheckedBox() if form_to_save.affect_flat else UncheckedBox(),
        'Blunted', CheckedBox() if form_to_save.affect_blunted else UncheckedBox(),
        'Expansive', CheckedBox() if form_to_save.affect_expansive else UncheckedBox(),
        'Agitated', CheckedBox() if form_to_save.affect_agitated else UncheckedBox()
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, None,
                                                                       None, 2.4 * inch])
    story.append(t)

    data = [[# 'Harmfulness:',
        'Self', CheckedBox() if form_to_save.harmfulness_self else UncheckedBox(),
        'Others', CheckedBox() if form_to_save.harmfulness_others else UncheckedBox(),
        'Negative Statements', CheckedBox() if form_to_save.harmfulness_negative_statements else UncheckedBox(),
        'Describe: ', 'test describe text',
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, 2.8 * inch])
    story.append(t)

    data = [[# 'Attention & Concentration:',
        'Good', CheckedBox() if form_to_save.attention_concentration_good else UncheckedBox(),
        'Fair', CheckedBox() if form_to_save.attention_concentration_fair else UncheckedBox(),
        'Poor', CheckedBox() if form_to_save.attention_concentration_poor else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, 4.5 * inch])
    story.append(t)

    data = [[# 'Orientation:',
        'Time', CheckedBox() if form_to_save.orientation_time else UncheckedBox(),
        'Place', CheckedBox() if form_to_save.orientation_place else UncheckedBox(),
        'Person', CheckedBox() if form_to_save.orientation_person else UncheckedBox(),
        'Disoriented', CheckedBox() if form_to_save.orientation_disoriented else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, 3.4 * inch])
    story.append(t)

    data = [[# 'Insight & Judgment:',
        'Good', CheckedBox() if form_to_save.insight_judgement_good else UncheckedBox(),
        'Fair', CheckedBox() if form_to_save.insight_judgement_fair else UncheckedBox(),
        'Poor', CheckedBox() if form_to_save.insight_judgement_poor else UncheckedBox()
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, 4.5 * inch])
    story.append(t)

    data = [[# 'Sleep Disturbances:',
        'Disturbance', CheckedBox() if form_to_save.sleep_disturbance else UncheckedBox(),
        'Apnea', CheckedBox() if form_to_save.sleep_disturbance_apnea else UncheckedBox(),
        'Narcolepsy', CheckedBox() if form_to_save.sleep_disturbance_narcolepsy else UncheckedBox(),
        'Nightmares', CheckedBox() if form_to_save.agg_behavior_physical else UncheckedBox(),
        'Hypnagogic / Hypnopompic Hallucinations', CheckedBox() if form_to_save.agg_behavior_physical else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, None, None, None,
                                                                       None, 0.4 * inch])
    story.append(t)

    data = [[# 'Appetite Change:',
        'No', CheckedBox() if form_to_save.appetite_change else UncheckedBox(),
        'Yes', CheckedBox() if form_to_save.appetite_change else UncheckedBox(),
        'Describe:', 'test describe text',
        'Tobacco Screen', CheckedBox() if form_to_save.tobacco_screen else UncheckedBox(),
        'Tele-Health', CheckedBox() if form_to_save.tele_health else UncheckedBox(),
    ]]
    t = Table(data, style=TableStyle(grid), hAlign=TA_LEFT, colWidths=[None, None, None, None,
                                                                       None, 2.35*inch, None, None,
                                                                       None, None])
    story.append(t)

    story.append(FrameBreak)

    p = Paragraph(f'Assessment:',
                  style=ParagraphStyle(name='Normal', fontName='Helvetica-Bold',
                                       fontSize=10, alignment=TA_LEFT))
    story.append(p)

    p = Paragraph(f'Diagnostic Impression:',
                  style=ParagraphStyle(name='Normal', leftIndent=5, fontName='Helvetica-Bold',
                                       fontSize=9, alignment=TA_LEFT))
    story.append(p)

    if form_to_save.diagnostic_impression:
        p = Paragraph(f'{form_to_save.diagnostic_impression}',
                      style=ParagraphStyle(name='Normal', leftIndent=15, fontName='Helvetica',
                                           fontSize=9, alignment=TA_LEFT))
        story.append(p)

    story.append(Spacer(0, 0.30 * inch))

    p = Paragraph(f'Plan:',
                  style=ParagraphStyle(name='Normal', fontName='Helvetica-Bold',
                                       fontSize=10, alignment=TA_LEFT))
    story.append(p)

    p = Paragraph(f'Current Medication:',
                  style=ParagraphStyle(name='Normal', leftIndent=5, fontName='Helvetica-Bold',
                                       fontSize=9, alignment=TA_LEFT))
    story.append(p)

    if form_to_save.current_medication:
        p = Paragraph(f'{form_to_save.current_medication}',
                      style=ParagraphStyle(name='Normal', leftIndent=15, fontName='Helvetica',
                                           fontSize=9, alignment=TA_LEFT))
        story.append(p)

    story.append(Spacer(0, 0.2 * inch))

    p = Paragraph(f'Discussion and Treatment Considerations:',
                  style=ParagraphStyle(name='Normal', leftIndent=5, fontName='Helvetica-Bold',
                                       fontSize=9, alignment=TA_LEFT))
    story.append(p)

    if form_to_save.discussion_treatment:
        p = Paragraph(f'{form_to_save.discussion_treatment}',
                      style=ParagraphStyle(name='Normal', leftIndent=15, fontName='Helvetica',
                                           fontSize=9, alignment=TA_LEFT))
        story.append(p)

    story.append(Spacer(0, 0.35 * inch))

    p = Paragraph(
        f'Signature:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{form_to_save.signature}',
        style=ParagraphStyle(name='Normal', leftIndent=0, fontName='Helvetica-Bold',
                             fontSize=9, alignment=TA_LEFT))
    story.append(p)

    p = Paragraph(
        f'Norman Hendricksen, Ph.D. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        f'[1] If in agreement with PCP, Risk-Benefit Analysis, IDT, RP',
        style=ParagraphStyle(name='Normal', leftIndent=64, fontName='Helvetica',
                             fontSize=9, alignment=TA_LEFT))
    story.append(p)

    # doc.build(story, onFirstPage=first_page)
    doc.build(story)
