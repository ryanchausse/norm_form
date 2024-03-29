# Generated by Django 3.2.8 on 2021-12-08 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0016_auto_20211129_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='LensDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=255)),
                ('promo_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('retail_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('static_img_url', models.CharField(default='multiple_lenses.jpg', max_length=255)),
                ('uploaded_img', models.ImageField(blank=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Lens Design',
                'verbose_name_plural': 'Lens Designs',
            },
        ),
    ]
