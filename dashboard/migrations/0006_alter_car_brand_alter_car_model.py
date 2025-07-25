# Generated by Django 5.2.2 on 2025-06-14 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_brand_carmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.brand'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.carmodel'),
        ),
    ]
