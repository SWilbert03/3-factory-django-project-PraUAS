from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view()),
    
    # Water Heater System
    path('sensor/sensor1', views.sensor11view.as_view()),
    path('sensor/sensor1', views.sensor12view.as_view()),
    path('sensor/sensor1', views.sensor13view.as_view()),
    path('actuator/actuator1', views.actuator1view.as_view()),
    
    # Fan Control System
    path('sensor/sensor2', views.sensor21view.as_view()),
    path('sensor/sensor2', views.sensor22view.as_view()),
    path('sensor/sensor2', views.sensor23view.as_view()),
    path('actuator/actuator2', views.actuator2view.as_view()),
    
    # Lighting Control System 
    path('sensor/sensor3', views.sensor31view.as_view()),
    path('sensor/sensor3', views.sensor32view.as_view()),
    path('sensor/sensor3', views.sensor33view.as_view()),
    path('actuator/actuator3', views.actuator3view.as_view()),
]