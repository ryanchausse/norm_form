# Generated by Django 3.2.8 on 2021-11-17 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_auto_20211117_0126'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerLensPackage',
            new_name='CustomerOrder',
        ),
        migrations.AlterModelOptions(
            name='customerorder',
            options={'verbose_name': 'Customer and their Order', 'verbose_name_plural': 'Customers and their Order'},
        ),
        migrations.RemoveField(
            model_name='lenspackage',
            name='lens_add_on',
        ),
        migrations.RemoveField(
            model_name='lenspackage',
            name='lens_material',
        ),
        migrations.RemoveField(
            model_name='lenspackage',
            name='lens_type',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('notes', models.CharField(max_length=255)),
                ('promo_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('retail_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='form.customer')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='LensPackageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lens_add_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.lensaddons')),
                ('lens_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.lensmaterial')),
                ('lens_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.lenspackage')),
                ('lens_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.lenstype')),
            ],
            options={
                'verbose_name': 'Lens Package Items',
                'verbose_name_plural': 'Lens Package Items',
            },
        ),
    ]
