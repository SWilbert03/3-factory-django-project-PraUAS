from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

import joblib
from machinelearning import mlmodel

from .models import Sensor, SensorLog, Actuator, ActuatorLog

class SensorTemplateView(APIView):
    sensor_name = ""
    def get(self, request, format=None):
        sensor = Sensor.objects.get(name=self.sensor_name)
        data = {
            "value": sensor.value
        }
        return Response(data)

class ActuatorTemplateView(APIView):
    actuator_name = ""
    sensor1_name  = ""
    sensor2_name  = ""
    sensor3_name  = ""
    training_csv  = ""
    def get(self, request, format=None):
        actuator = Actuator.objects.get(name=self.actuator_name)
        sensor1  = Sensor.objects.get(name=self.sensor1_name)
        sensor2  = Sensor.objects.get(name=self.sensor2_name)
        sensor3  = Sensor.objects.get(name=self.sensor3_name)
        model = mlmodel.BaseLinearRegression(settings.ML_ROOT + self.training_csv)
        prediction = model.predict([float(sensor1.value), float(sensor2.value), float(sensor3.value)])
        actuator.state = int(prediction)
        actuator.save()
        data = {
            "state": actuator.state
        }
        return Response(data)

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

# subsistem1
class sensor11view(SensorTemplateView):
    sensor_name = "sensor11"
    
class sensor12view(SensorTemplateView):
    sensor_name = "sensor12"

class sensor13view(SensorTemplateView):
    sensor_name = "sensor13"
    
class actuator1view(ActuatorTemplateView):
    actuator_name = "actuator1"
    sensor1_name = "sensor11"
    sensor2_name = "sensor12"
    sensor3_name = "sensor13"
    training_csv = "heater.csv"

# subsistem2
class sensor21view(SensorTemplateView):
    sensor_name = "sensor21"
    
class sensor22view(SensorTemplateView):
    sensor_name = "sensor22"
    
class sensor23view(SensorTemplateView):
    sensor_name = "sensor23"
    
class actuator2view(ActuatorTemplateView):
    actuator_name = "actuator2"
    sensor1_name = "sensor21"
    sensor2_name = "sensor22"
    sensor3_name = "sensor23"
    training_csv = "fan.csv"
    
# subsistem3
class sensor31view(SensorTemplateView):
    sensor_name = "sensor31"
    
class sensor32view(SensorTemplateView):
    sensor_name = "sensor32"
    
class sensor33view(SensorTemplateView):
    sensor_name = "sensor33"

class actuator3view(ActuatorTemplateView):
    actuator_name = "actuator3"
    sensor1_name = "sensor31"
    sensor2_name = "sensor32"
    sensor3_name = "sensor33"
    training_csv = "light.csv"