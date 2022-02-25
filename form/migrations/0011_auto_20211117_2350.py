# Generated by Django 3.2.8 on 2021-11-17 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_alter_lenspackageitem_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='promo_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='retail_price',
        ),
        migrations.AddField(
            model_name='order',
            name='lens_package',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='form.lenspackage'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='form.customer'),
        ),
        migrations.DeleteModel(
            name='CustomerOrder',
        ),
    ]