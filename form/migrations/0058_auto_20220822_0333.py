# Generated by Django 3.2.8 on 2022-08-22 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('form', '0057_normform_bal_accessed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='form.facility')),
            ],
            options={
                'verbose_name': 'Physician',
                'verbose_name_plural': 'Physicians',
            },
        ),
        migrations.AddField(
            model_name='normform',
            name='physician',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='form.physician'),
        ),
    ]