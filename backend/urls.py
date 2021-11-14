from django.urls import path, include
from django.urls.resolvers import URLPattern
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'Individual_appointment', views.Individual_appointment_viewset)
#URLConf
urlpatterns =[
    path('hello/',views.say_hello),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]