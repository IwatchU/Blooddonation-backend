# Generated by Django 3.2.9 on 2021-11-14 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Individual_appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation', models.BooleanField()),
                ('booked', models.BooleanField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='blood_donation_free_appointments',
            name='Date_time',
        ),
        migrations.RemoveField(
            model_name='blood_donation_free_appointments',
            name='num_pacients',
        ),
        migrations.RemoveField(
            model_name='blood_donation_free_appointments',
            name='num_taken',
        ),
        migrations.AddField(
            model_name='blood_donation_free_appointments',
            name='day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='blood_donation_free_appointments',
            name='hour',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='blood_donation_free_appointments',
            name='minute',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='blood_donation_free_appointments',
            name='month',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='blood_donation_free_appointments',
            name='number_available',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='blood_donation_free_appointments',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
