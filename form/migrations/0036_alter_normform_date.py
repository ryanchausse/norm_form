# Generated by Django 3.2.8 on 2022-03-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0035_auto_20220225_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normform',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
