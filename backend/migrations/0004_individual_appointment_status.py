# Generated by Django 3.2.9 on 2021-11-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_individual_appointment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual_appointment',
            name='status',
            field=models.TextField(default='no status'),
        ),
    ]
