from django import forms
from django.forms import SelectDateWidget
from .models import NormForm
import datetime
from .models import Patient
from .models import Facility


class NormFormForm(forms.Form):
    name = forms.CharField(max_length=60)
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    facility = forms.ModelChoiceField(queryset=Facility.objects.all())
    date = forms.DateField(initial=datetime.date.today())

    # Subjective
    chief_complaints_problems_history = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 80, 'rows': 7}))

    # Objective - staff / other sources reported
    agg_behavior_physical = forms.BooleanField()
    agg_behavior_verbal = forms.BooleanField()
    agg_behavior_gestures = forms.BooleanField()
    agg_behavior_threatening = forms.BooleanField()
    agg_behavior_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    gen_appearance_well_groomed = forms.BooleanField()
    gen_appearance_fairly_groomed = forms.BooleanField()
    gen_appearance_poorly_groomed = forms.BooleanField()
    gen_appearance_disheveled = forms.BooleanField()
    gen_appearance_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    treat_and_compliance_acceptable = forms.BooleanField()
    treat_and_compliance_low_motivation = forms.BooleanField()
    treat_and_compliance_resistive = forms.BooleanField()
    treat_and_compliance_argumentative = forms.BooleanField()
    treat_and_compliance_exit_seeking = forms.BooleanField()
    treat_and_compliance_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    inappropriate_behavior = forms.BooleanField()
    inappropriate_behavior_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    attitude_cooperative = forms.BooleanField()
    attitude_uncooperative = forms.BooleanField()
    attitude_marginally_cooperative = forms.BooleanField()
    attitude_other = forms.BooleanField()
    attitude_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    speech_intact = forms.BooleanField()
    speech_pressured = forms.BooleanField()
    speech_hyperverbal = forms.BooleanField()
    speech_loud = forms.BooleanField()
    speech_slow = forms.BooleanField()
    speech_unintelligible = forms.BooleanField()
    speech_yelling_out = forms.BooleanField()
    speech_perseverative = forms.BooleanField()
    speech_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    verbal_abilities_receptive_language_sufficient = forms.BooleanField()
    verbal_abilities_receptive_language_impaired = forms.BooleanField()
    verbal_abilities_expressive_language_sufficient = forms.BooleanField()
    verbal_abilities_expressive_language_impaired = forms.BooleanField()
    verbal_abilities_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    communication_verbal = forms.BooleanField()
    communication_non_verbal = forms.BooleanField()
    communication_minimally_verbal = forms.BooleanField()
    communication_withdrawn = forms.BooleanField()
    communication_avoidant = forms.BooleanField()
    communication_evasive = forms.BooleanField()
    communication_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    perceptual_disturbances_none = forms.BooleanField()
    perceptual_disturbances_hallucinations = forms.BooleanField()
    perceptual_disturbances_visual = forms.BooleanField()
    perceptual_disturbances_auditory = forms.BooleanField()
    perceptual_disturbances_command = forms.BooleanField()
    perceptual_disturbances_tactile = forms.BooleanField()
    perceptual_disturbances_olfactory = forms.BooleanField()
    perceptual_disturbances_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    level_of_consciousness_alert = forms.BooleanField()
    level_of_consciousness_confused = forms.BooleanField()
    level_of_consciousness_drowsy = forms.BooleanField()
    level_of_consciousness_somnolent = forms.BooleanField()
    level_of_consciousness_fluctuating = forms.BooleanField()
    level_of_consciousness_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    thought_process_linear = forms.BooleanField()
    thought_process_disorganized = forms.BooleanField()
    thought_process_fragmented = forms.BooleanField()
    thought_process_racing = forms.BooleanField()
    thought_process_circumstantial = forms.BooleanField()
    thought_process_tangential = forms.BooleanField()
    thought_process_blocking = forms.BooleanField()
    thought_process_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    thought_content_normal = forms.BooleanField()
    thought_content_delusions = forms.BooleanField()
    thought_content_persecutory = forms.BooleanField()
    thought_content_grandiose = forms.BooleanField()
    thought_content_religious = forms.BooleanField()
    thought_content_self_referential = forms.BooleanField()
    thought_content_poverty_of_content = forms.BooleanField()
    thought_content_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    mood_euthymic = forms.BooleanField()
    mood_depressed = forms.BooleanField()
    mood_anxious = forms.BooleanField()
    mood_irritable = forms.BooleanField()
    mood_angry = forms.BooleanField()
    mood_tearful = forms.BooleanField()
    mood_elated = forms.BooleanField()
    mood_labile = forms.BooleanField()
    mood_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    affect_appropriate = forms.BooleanField()
    affect_flat = forms.BooleanField()
    affect_blunted = forms.BooleanField()
    affect_expansive = forms.BooleanField()
    affect_agitated = forms.BooleanField()
    affect_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    harmfulness_self = forms.BooleanField()
    harmfulness_others = forms.BooleanField()
    harmfulness_negative_statements = forms.BooleanField()
    harmfulness_other = forms.BooleanField()
    harmfulness_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    attention_concentration_good = forms.BooleanField()
    attention_concentration_fair = forms.BooleanField()
    attention_concentration_poor = forms.BooleanField()
    attention_concentration_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    orientation_time = forms.BooleanField()
    orientation_place = forms.BooleanField()
    orientation_person = forms.BooleanField()
    orientation_situation = forms.BooleanField()
    orientation_disoriented = forms.BooleanField()
    orientation_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    insight_judgement_good = forms.BooleanField()
    insight_judgement_fair = forms.BooleanField()
    insight_judgement_poor = forms.BooleanField()
    insight_judgement_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    sleep_disturbance = forms.BooleanField()
    sleep_disturbance_apnea = forms.BooleanField()
    sleep_disturbance_narcolepsy = forms.BooleanField()
    sleep_disturbance_describe = forms.BooleanField()
    sleep_disturbance_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    appetite_change = forms.BooleanField()
    appetite_change_notes = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    # Misc
    tobacco_screen = forms.BooleanField()
    tele_health = forms.BooleanField()

    # Assessment
    diagnostic_impression = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 80, 'rows': 7}))

    # Plan
    current_medication = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 80, 'rows': 7}))
    discussion_treatment = forms.CharField(max_length=50000, widget=forms.Textarea(attrs={'cols': 80, 'rows': 7}))

    signature = forms.CharField(max_length=500)

