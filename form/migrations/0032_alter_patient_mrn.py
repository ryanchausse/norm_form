# Generated by Django 3.2.8 on 2022-02-25 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0031_auto_20220225_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='mrn',
            field=models.IntegerField(default=None, null=True),
        ),
    ]