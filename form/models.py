from django.db import models
from django.core.validators import ValidationError
from django.db.models import Q


class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    mrn = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class NormForm(models.Model):
    name = models.CharField(max_length=60)
    patient = models.ForeignKey(Patient, default=None, on_delete=models.CASCADE)
    appearance = models.CharField(max_length=2000, null=True, default='')
    notes = models.CharField(max_length=2000, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Norm Form'
        verbose_name_plural = 'Norm Forms'
