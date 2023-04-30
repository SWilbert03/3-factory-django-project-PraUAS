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
    client.subscribe('sensor1/#')
    client.subscribe('sensor2/#')
    client.subscribe('sensor3/#')

on_message_sensor11 = on_message_mqtt('sensor11')
on_message_sensor12 = on_message_mqtt('sensor12')
on_message_sensor13 = on_message_mqtt('sensor13')

on_message_sensor21 = on_message_mqtt('sensor21')
on_message_sensor22 = on_message_mqtt('sensor22')
on_message_sensor23 = on_message_mqtt('sensor23')

on_message_sensor31 = on_message_mqtt('sensor31')
on_message_sensor32 = on_message_mqtt('sensor32')
on_message_sensor33 = on_message_mqtt('sensor33')

client = mqtt.Client()

client.message_callback_add('sensor1/sensor11', on_message_sensor11)
client.message_callback_add('sensor1/sensor12', on_message_sensor12)
client.message_callback_add('sensor1/sensor13', on_message_sensor13)

client.message_callback_add('sensor2/sensor21', on_message_sensor21)
client.message_callback_add('sensor2/sensor22', on_message_sensor22)
client.message_callback_add('sensor2/sensor23', on_message_sensor23)

client.message_callback_add('sensor3/sensor31', on_message_sensor31)
client.message_callback_add('sensor3/sensor32', on_message_sensor32)
client.message_callback_add('sensor3/sensor33', on_message_sensor33)

client.on_connect = on_connect

client.connect(settings.MQTT_HOST, settings.MQTT_PORT)
