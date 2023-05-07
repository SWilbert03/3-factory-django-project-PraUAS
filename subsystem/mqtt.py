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
    client.subscribe('musim/#')
    client.subscribe('hasilpenjualanberfluktuasi/#')
    client.subscribe('jumlahpengunjungrestoran/#')

#sistem 1

on_message_sensor111 = on_message_mqtt('Sensor Suhu')
on_message_sensor112 = on_message_mqtt('Sensor Kelembapan')
on_message_sensor113 = on_message_mqtt('Sensor pH')

on_message_sensor121 = on_message_mqtt('Sensor Oksigen')
on_message_sensor122 = on_message_mqtt('Sensor Kadar Garam')
on_message_sensor123 = on_message_mqtt('Sensor Kadar Lemak')

on_message_sensor131 = on_message_mqtt('Sensor Kadar Sodium')
on_message_sensor132 = on_message_mqtt('Sensor Kadar Protein')
on_message_sensor133 = on_message_mqtt('Sensor Kadar Gula')

#sistem 2
on_message_sensor211 = on_message_mqtt('Sensor Kelembapan Tanah')
on_message_sensor212 = on_message_mqtt('Sensor Intensi Cahaya')
on_message_sensor213 = on_message_mqtt('Sensor Suhu Udara')

on_message_sensor221 = on_message_mqtt('Sensor Suhu Tanah')
on_message_sensor222 = on_message_mqtt('Sensor Kelembapan Udara')
on_message_sensor223 = on_message_mqtt('Sensor Kadar Co2')

on_message_sensor231 = on_message_mqtt('Kecepatan Angin')
on_message_sensor232 = on_message_mqtt('Curah Hujan')
on_message_sensor233 = on_message_mqtt('Kualitas Air')

#sistem 3
on_message_sensor311 = on_message_mqtt('Sensor Barometer')
on_message_sensor312 = on_message_mqtt('Sensor Ketebalan Awan')
on_message_sensor313 = on_message_mqtt('Sensor Radiasi Surya')

on_message_sensor321 = on_message_mqtt('Sensor Cancel Order')
on_message_sensor322 = on_message_mqtt('Sensor Penilaian')
on_message_sensor323 = on_message_mqtt('Sensor Jumlah Pesanan')

on_message_sensor331 = on_message_mqtt('Sensor Pendeteksi Gerakan')
on_message_sensor332 = on_message_mqtt('Sensor Meja Kosong')
on_message_sensor333 = on_message_mqtt('Sensor Kebisingan')

client = mqtt.Client()

#=============================================================================================

#sistem 1
client.message_callback_add('susuhewanidantelur/sensorsuhu', on_message_sensor111)
client.message_callback_add('susuhewanidantelur/sensorkelembapan', on_message_sensor112)
client.message_callback_add('susuhewanidantelur/sensorph', on_message_sensor113)

client.message_callback_add('dagingmerah/sensoroksigen', on_message_sensor121)
client.message_callback_add('dagingmerah/sensorkadrgaram', on_message_sensor122)
client.message_callback_add('dagingmerah/sensorkadarlemak', on_message_sensor123)

client.message_callback_add('dagingputih/sensorkadarsodium', on_message_sensor131)
client.message_callback_add('dagingputih/sensorkadarprotein', on_message_sensor132)
client.message_callback_add('dagingputih/sensorkadargula', on_message_sensor133)

#sistem2
client.message_callback_add('sensorkarbohidrat/kelembapantanah', on_message_sensor211)
client.message_callback_add('sensorkarbohidrat/intensicahaya', on_message_sensor212)
client.message_callback_add('sensorkarbohidrat/suhuudara', on_message_sensor213)

client.message_callback_add('sayuran/suhutanah', on_message_sensor221)
client.message_callback_add('sayuran/sensorkelembapanudara', on_message_sensor222)
client.message_callback_add('sayuran/sensorkadarco2', on_message_sensor223)

client.message_callback_add('buah/sensorkecepatanangin', on_message_sensor231)
client.message_callback_add('buah/sensorcurahhujan', on_message_sensor232)
client.message_callback_add('buah/sensorkualitasair', on_message_sensor233)

#sistem3
client.message_callback_add('musim/barometer', on_message_sensor311)
client.message_callback_add('musim/ketebalanawan', on_message_sensor312)
client.message_callback_add('musim/radiasisurya', on_message_sensor313)

client.message_callback_add('hasilpenjualanberfluktuasi/cancelorder', on_message_sensor321)
client.message_callback_add('hasilpenjualanberfluktuasi/penilaian', on_message_sensor322)
client.message_callback_add('hasilpenjualanberfluktuasi/jumlahpesanan', on_message_sensor323)

client.message_callback_add('jumlahpengunjungrestoran/pendeteksigerakan', on_message_sensor331)
client.message_callback_add('jumlahpengunjungrestoran/mejakosong', on_message_sensor332)
client.message_callback_add('jumlahpengunjungrestoran/kebisingan', on_message_sensor333)

client.on_connect = on_connect

client.connect(settings.MQTT_HOST, settings.MQTT_PORT)
