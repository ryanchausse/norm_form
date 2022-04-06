from django.contrib import admin
from .models import NormForm
from .models import Patient
from .models import Facility
from .models import SubjectiveOption
from .models import DiscussionTreatmentOption

admin.site.register(NormForm)
admin.site.register(Patient)
admin.site.register(Facility)
admin.site.register(SubjectiveOption)
admin.site.register(DiscussionTreatmentOption)
