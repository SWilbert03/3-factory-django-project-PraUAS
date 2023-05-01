from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view()),
    
    # Water Heater System
    path('sensor/sensor11', views.sensor11view.as_view()),
    path('sensor/sensor12', views.sensor12view.as_view()),
    path('sensor/sensor13', views.sensor13view.as_view()),
    path('actuator/actuator1', views.actuator1view.as_view()),
    
    # Fan Control System
    path('sensor/sensor21', views.sensor21view.as_view()),
    path('sensor/sensor22', views.sensor22view.as_view()),
    path('sensor/sensor23', views.sensor23view.as_view()),
    path('actuator/actuator2', views.actuator2view.as_view()),
    
    # Lighting Control System 
    path('sensor/sensor31', views.sensor31view.as_view()),
    path('sensor/sensor32', views.sensor32view.as_view()),
    path('sensor/sensor33', views.sensor33view.as_view()),
    path('actuator/actuator3', views.actuator3view.as_view()),
]