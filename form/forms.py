from django import forms
from django.forms import SelectDateWidget
from .models import NormForm
import datetime
from .models import Patient
from .models import Facility


class NormFormForm(forms.ModelForm):
    name = forms.CharField(required=False, max_length=500, widget=forms.TextInput(attrs={'size': 80}))
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    facility = forms.ModelChoiceField(queryset=Facility.objects.all())
    date = forms.DateField(initial=datetime.date.today())

    # Subjective
    chief_complaints_problems_history = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 80, 'rows': 7}))

    # Objective - staff / other sources reported
    agg_behavior_physical = forms.BooleanField(required=False)
    agg_behavior_verbal = forms.BooleanField(required=False)
    agg_behavior_gestures = forms.BooleanField(required=False)
    agg_behavior_threatening = forms.BooleanField(required=False)
    agg_behavior_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    gen_appearance_well_groomed = forms.BooleanField(required=False)
    gen_appearance_fairly_groomed = forms.BooleanField(required=False)
    gen_appearance_poorly_groomed = forms.BooleanField(required=False)
    gen_appearance_disheveled = forms.BooleanField(required=False)
    gen_appearance_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    treat_and_compliance_acceptable = forms.BooleanField(required=False)
    treat_and_compliance_low_motivation = forms.BooleanField(required=False)
    treat_and_compliance_resistive = forms.BooleanField(required=False)
    treat_and_compliance_argumentative = forms.BooleanField(required=False)
    treat_and_compliance_exit_seeking = forms.BooleanField(required=False)
    treat_and_compliance_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    inappropriate_behavior = forms.BooleanField(required=False)
    inappropriate_behavior_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    attitude_cooperative = forms.BooleanField(required=False)
    attitude_uncooperative = forms.BooleanField(required=False)
    attitude_marginally_cooperative = forms.BooleanField(required=False)
    attitude_other = forms.BooleanField(required=False)
    attitude_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    speech_intact = forms.BooleanField(required=False)
    speech_pressured = forms.BooleanField(required=False)
    speech_hyperverbal = forms.BooleanField(required=False)
    speech_loud = forms.BooleanField(required=False)
    speech_slow = forms.BooleanField(required=False)
    speech_unintelligible = forms.BooleanField(required=False)
    speech_yelling_out = forms.BooleanField(required=False)
    speech_perseverative = forms.BooleanField(required=False)
    speech_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    verbal_abilities_receptive_language_sufficient = forms.BooleanField(required=False)
    verbal_abilities_receptive_language_impaired = forms.BooleanField(required=False)
    verbal_abilities_expressive_language_sufficient = forms.BooleanField(required=False)
    verbal_abilities_expressive_language_impaired = forms.BooleanField(required=False)
    verbal_abilities_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    communication_verbal = forms.BooleanField(required=False)
    communication_non_verbal = forms.BooleanField(required=False)
    communication_minimally_verbal = forms.BooleanField(required=False)
    communication_withdrawn = forms.BooleanField(required=False)
    communication_avoidant = forms.BooleanField(required=False)
    communication_evasive = forms.BooleanField(required=False)
    communication_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    perceptual_disturbances_none = forms.BooleanField(required=False)
    perceptual_disturbances_hallucinations = forms.BooleanField(required=False)
    perceptual_disturbances_visual = forms.BooleanField(required=False)
    perceptual_disturbances_auditory = forms.BooleanField(required=False)
    perceptual_disturbances_command = forms.BooleanField(required=False)
    perceptual_disturbances_tactile = forms.BooleanField(required=False)
    perceptual_disturbances_olfactory = forms.BooleanField(required=False)
    perceptual_disturbances_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    level_of_consciousness_alert = forms.BooleanField(required=False)
    level_of_consciousness_confused = forms.BooleanField(required=False)
    level_of_consciousness_drowsy = forms.BooleanField(required=False)
    level_of_consciousness_somnolent = forms.BooleanField(required=False)
    level_of_consciousness_fluctuating = forms.BooleanField(required=False)
    level_of_consciousness_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    thought_process_linear = forms.BooleanField(required=False)
    thought_process_disorganized = forms.BooleanField(required=False)
    thought_process_fragmented = forms.BooleanField(required=False)
    thought_process_racing = forms.BooleanField(required=False)
    thought_process_circumstantial = forms.BooleanField(required=False)
    thought_process_tangential = forms.BooleanField(required=False)
    thought_process_blocking = forms.BooleanField(required=False)
    thought_process_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    thought_content_normal = forms.BooleanField(required=False)
    thought_content_delusions = forms.BooleanField(required=False)
    thought_content_persecutory = forms.BooleanField(required=False)
    thought_content_grandiose = forms.BooleanField(required=False)
    thought_content_religious = forms.BooleanField(required=False)
    thought_content_self_referential = forms.BooleanField(required=False)
    thought_content_poverty_of_content = forms.BooleanField(required=False)
    thought_content_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    mood_euthymic = forms.BooleanField(required=False)
    mood_depressed = forms.BooleanField(required=False)
    mood_anxious = forms.BooleanField(required=False)
    mood_irritable = forms.BooleanField(required=False)
    mood_angry = forms.BooleanField(required=False)
    mood_tearful = forms.BooleanField(required=False)
    mood_elated = forms.BooleanField(required=False)
    mood_labile = forms.BooleanField(required=False)
    mood_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    affect_appropriate = forms.BooleanField(required=False)
    affect_flat = forms.BooleanField(required=False)
    affect_blunted = forms.BooleanField(required=False)
    affect_expansive = forms.BooleanField(required=False)
    affect_agitated = forms.BooleanField(required=False)
    affect_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    harmfulness_self = forms.BooleanField(required=False)
    harmfulness_others = forms.BooleanField(required=False)
    harmfulness_negative_statements = forms.BooleanField(required=False)
    harmfulness_other = forms.BooleanField(required=False)
    harmfulness_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    attention_concentration_good = forms.BooleanField(required=False)
    attention_concentration_fair = forms.BooleanField(required=False)
    attention_concentration_poor = forms.BooleanField(required=False)
    attention_concentration_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    orientation_time = forms.BooleanField(required=False)
    orientation_place = forms.BooleanField(required=False)
    orientation_person = forms.BooleanField(required=False)
    orientation_situation = forms.BooleanField(required=False)
    orientation_disoriented = forms.BooleanField(required=False)
    orientation_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    insight_judgement_good = forms.BooleanField(required=False)
    insight_judgement_fair = forms.BooleanField(required=False)
    insight_judgement_poor = forms.BooleanField(required=False)
    insight_judgement_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    sleep_disturbance = forms.BooleanField(required=False)
    sleep_disturbance_apnea = forms.BooleanField(required=False)
    sleep_disturbance_narcolepsy = forms.BooleanField(required=False)
    sleep_disturbance_describe = forms.BooleanField(required=False)
    sleep_disturbance_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    appetite_change = forms.BooleanField(required=False)
    appetite_change_notes = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}))

    # Misc
    tobacco_screen = forms.BooleanField(required=False)
    tele_health = forms.BooleanField(required=False)

    # Assessment
    diagnostic_impression = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 80, 'rows': 7}))

    # Plan
    current_medication = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 80, 'rows': 7}))
    discussion_treatment = forms.CharField(required=False, max_length=50000, widget=forms.Textarea(attrs={'cols': 80, 'rows': 7}))

    signature = forms.CharField(max_length=500)

    class Meta:
        model = NormForm
        exclude = ['created_by']
