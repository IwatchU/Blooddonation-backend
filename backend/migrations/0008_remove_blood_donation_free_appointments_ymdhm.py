# Generated by Django 3.2.9 on 2021-11-14 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_blood_donation_free_appointments_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blood_donation_free_appointments',
            name='ymdhm',
        ),
    ]
