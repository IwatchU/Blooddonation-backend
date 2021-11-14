from django.shortcuts import render
from django.http import HttpResponse
from .models import Individual_appointment,blood_donation_free_appointments
from .serializers import Individual_appointment_serializer
from rest_framework import viewsets

# request handler
# Create your views here.
# request --> response

def say_hello (request):
    #Pull data
    return render(request,'hello.html')

class Individual_appointment_viewset(viewsets.ModelViewSet):
    queryset=Individual_appointment.objects.all()
    serializer_class=Individual_appointment_serializer