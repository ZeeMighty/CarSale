# Generated by Django 5.2.2 on 2025-06-13 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
