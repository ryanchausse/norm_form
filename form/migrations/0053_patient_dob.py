# Generated by Django 3.2.8 on 2022-04-29 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0052_alter_normform_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
    ]