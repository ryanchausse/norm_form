# Generated by Django 3.2.8 on 2022-05-20 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0056_normform_emailed'),
    ]

    operations = [
        migrations.AddField(
            model_name='normform',
            name='bal_accessed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
