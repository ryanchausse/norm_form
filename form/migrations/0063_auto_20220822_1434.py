# Generated by Django 3.2.8 on 2022-08-22 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0062_alter_physician_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normform',
            name='physician',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Physician',
        ),
    ]
