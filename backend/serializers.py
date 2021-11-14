from rest_framework import serializers
from .models import blood_donation_free_appointments, Individual_appointment

class Individual_appointment_serializer(serializers.ModelSerializer):
    class Meta:
        model=Individual_appointment
        fields=('id','reservation', 'booked', 'status', 'appointment_time')
        