# Generated by Django 3.2.8 on 2022-04-26 22:55

from django.db import migrations
import jsignature.fields


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0051_remove_normform_sleep_disturbance_describe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normform',
            name='signature',
            field=jsignature.fields.JSignatureField(default=None),
            preserve_default=False,
        ),
    ]
