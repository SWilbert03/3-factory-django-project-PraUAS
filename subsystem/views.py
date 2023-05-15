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

# Smart Farm ==========================================================================================================================================
# 	Susu Hewani dan Telur
class SensorSuhuView(SensorTemplateView):
    sensor_name = "Sensor Suhu"
    
class SensorKelembapanView(SensorTemplateView):
    sensor_name = "Sensor Kelembapan"

class SensorpHView(SensorTemplateView):
    sensor_name = "Sensor pH"
    
class actuator1view(ActuatorTemplateView):
    actuator_name = "actuator1"
    sensor1_name = "Sensor Suhu"
    sensor2_name = "Sensor Kelembapan"
    sensor3_name = "Sensor pH"
    training_csv = "heater.csv"

# Daging Merah
class SensorOksigenView(SensorTemplateView):
    sensor_name = "Sensor Oksigen"
    
class SensorKadarGaramView(SensorTemplateView):
    sensor_name = "Sensor Kadar Garam"
    
class SensorKadarLemakView(SensorTemplateView):
    sensor_name = "Sensor Kadar Lemak"
    
class actuator2view(ActuatorTemplateView):
    actuator_name = "actuator2"
    sensor1_name = "Sensor Oksigen"
    sensor2_name = "Sensor Kadar Garam"
    sensor3_name = "Sensor Kadar Lemak"
    training_csv = "fan.csv"
    
# Daging Putih
class SensorKadarSodiumView(SensorTemplateView):
    sensor_name = "Sensor Kadar Sodium"
    
class SensorKadarProteinView(SensorTemplateView):
    sensor_name = "Sensor Kadar Protein"
    
class SensorKadarGulaView(SensorTemplateView):
    sensor_name = "Sensor Kadar Gula"

class actuator3view(ActuatorTemplateView):
    actuator_name = "actuator3"
    sensor1_name = "Sensor Kadar Sodium"
    sensor2_name = "Sensor Kadar Protein"
    sensor3_name = "Sensor Kadar Gula"
    training_csv = "light.csv"

# Smart Plantation ==========================================================================================================================================
# 	Sumber Karbohidrat
class SensorKelembapanTanahView(SensorTemplateView):
    sensor_name = "Sensor Kelembapan Tanah"
    
class SensorIntensiCahayaView(SensorTemplateView):
    sensor_name = "Sensor Intensi Cahaya"

class SensorSuhuUdaraView(SensorTemplateView):
    sensor_name = "Sensor Suhu Udara"
    
class actuator4view(ActuatorTemplateView):
    actuator_name = "actuator4"
    sensor1_name = "Sensor Kelembapan Tanah"
    sensor2_name = "Sensor Intensi Cahaya"
    sensor3_name = "Sensor Suhu Udara"
    training_csv = "heater.csv"

# Sayuran
class SensorSuhuTanahView(SensorTemplateView):
    sensor_name = "Sensor Suhu Tanah"
    
class SensorKelembapanUdaraView(SensorTemplateView):
    sensor_name = "Sensor Kelembapan Udara"
    
class SensorKadarCo2View(SensorTemplateView):
    sensor_name = "Sensor Kadar Co2"
    
class actuator5view(ActuatorTemplateView):
    actuator_name = "actuator5"
    sensor1_name = "Sensor Suhu Tanah"
    sensor2_name = "Sensor Kelembapan Udara"
    sensor3_name = "Sensor Kadar Co2"
    training_csv = "fan.csv"
    
# Buah-buahan
class KecepatanAnginView(SensorTemplateView):
    sensor_name = "Kecepatan Angin"
    
class CurahHujanView(SensorTemplateView):
    sensor_name = "Curah Hujan"
    
class KualitasAirView(SensorTemplateView):
    sensor_name = "Kualitas Air"

class actuator6view(ActuatorTemplateView):
    actuator_name = "actuator6"
    sensor1_name = "Kecepatan Angin"
    sensor2_name = "Curah Hujan"
    sensor3_name = "Kualitas Air"
    training_csv = "light.csv"

# Smart Restaurant ==========================================================================================================================================
# DeteKsi Musim
class SensorBarometerView(SensorTemplateView):
    sensor_name = "Sensor Barometer"
    
class SensorKetebalanAwanView(SensorTemplateView):
    sensor_name = "Sensor Ketebalan Awan"

class SensorRadiasiSuryaView(SensorTemplateView):
    sensor_name = "Sensor Radiasi Surya"
    
class actuator7view(ActuatorTemplateView):
    actuator_name = "actuator7"
    sensor1_name = "Sensor Barometer"
    sensor2_name = "Sensor Ketebalan Awan"
    sensor3_name = "Sensor Radiasi Surya"
    training_csv = "heater.csv"

# Deteksi Hasil Penjualan Berfluktuasi
class SensorCancelOrderView(SensorTemplateView):
    sensor_name = "Sensor Cancel Order"
    
class SensorPenilaianView(SensorTemplateView):
    sensor_name = "Sensor Penilaian"
    
class SensorJumlahPesananView(SensorTemplateView):
    sensor_name = "Sensor Jumlah Pesanan"
    
class actuator8view(ActuatorTemplateView):
    actuator_name = "actuator8"
    sensor1_name = "Sensor Cancel Order"
    sensor2_name = "Sensor Penilaian"
    sensor3_name = "Sensor Jumlah Pesanan"
    training_csv = "fan.csv"
    
# Deteksi Jumlah Pengunjung Restoran
class SensorPendeteksiGerakanView(SensorTemplateView):
    sensor_name = "Sensor Pendeteksi Gerakan"
    
class SensorMejaKosongView(SensorTemplateView):
    sensor_name = "Sensor Meja Kosong"
    
class SensorKebisinganView(SensorTemplateView):
    sensor_name = "Sensor Kebisingan"

class actuator9view(ActuatorTemplateView):
    actuator_name = "actuator9"
    sensor1_name = "Sensor Pendeteksi Gerakan"
    sensor2_name = "Sensor Meja Kosong"
    sensor3_name = "Sensor Kebisingan"
    training_csv = "light.csv"