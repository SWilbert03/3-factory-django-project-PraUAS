import paho.mqtt.client as mqtt
from django.conf import settings

from .models import Sensor, SensorLog

def on_message_mqtt(sensor_name):
    def template(client, userdata, msg):
        sen = Sensor.objects.get(name=sensor_name)
        sen.value = msg.payload.decode('utf-8')
        sen.save()
        sen_log = SensorLog(name=sen, value=msg.payload.decode('utf-8'))
        sen_log.save()
    return template

def on_connect(client, userdata, rc, result):
    client.subscribe('susuhewanidantelur/#')
    client.subscribe('dagingmerah/#')
    client.subscribe('dagingputih/#')
    client.subscribe('sensorkarbohidrat/#')
    client.subscribe('sayuran/#')
    client.subscribe('buah/#')

on_message_sensor111 = on_message_mqtt('Sensor Suhu')
on_message_sensor112 = on_message_mqtt('Sensor Kelembapan')
on_message_sensor113 = on_message_mqtt('Sensor pH')

on_message_sensor121 = on_message_mqtt('Sensor Oksigen')
on_message_sensor122 = on_message_mqtt('Sensor Kadar Garam')
on_message_sensor123 = on_message_mqtt('Sensor Kadar Lemak')

on_message_sensor131 = on_message_mqtt('Sensor Kadar Sodium')
on_message_sensor132 = on_message_mqtt('Sensor Kadar Protein')
on_message_sensor133 = on_message_mqtt('Sensor Kadar Gula')

client = mqtt.Client()

client.message_callback_add('susuhewanidantelur/sensorsuhu', on_message_sensor111)
client.message_callback_add('susuhewanidantelur/sensorkelembapan', on_message_sensor112)
client.message_callback_add('susuhewanidantelur/sensorph', on_message_sensor113)

client.message_callback_add('dagingmerah/sensoroksigen', on_message_sensor121)
client.message_callback_add('dagingmerah/sensorkadrgaram', on_message_sensor122)
client.message_callback_add('dagingmerah/sensorkadarlemak', on_message_sensor123)

client.message_callback_add('dagingputih/sensorkadarsodium', on_message_sensor131)
client.message_callback_add('dagingputih/sensorkadarprotein', on_message_sensor132)
client.message_callback_add('dagingputih/sensorkadargula', on_message_sensor133)

client.on_connect = on_connect

client.connect(settings.MQTT_HOST, settings.MQTT_PORT)
