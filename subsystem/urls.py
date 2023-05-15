from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view()),

#Smart Farm
    # Susu Hewani dan Telur
    path('susuhewanidantelur/sensorsuhu', views.SensorSuhuView.as_view()),
    path('susuhewanidantelur/sensorkelembapan', views.SensorKelembapanView.as_view()),
    path('susuhewanidantelur/sensorph', views.SensorpHView.as_view()),
    path('actuator/actuator1', views.actuator1view.as_view()),
    
    # Daging Merah
    path('dagingmerah/sensoroksigen', views.SensorOksigenView.as_view()),
    path('dagingmerah/sensorkadrgaram', views.SensorKadarGaramView.as_view()),
    path('dagingmerah/sensorkadarlemak', views.SensorKadarLemakView.as_view()),
    path('actuator/actuator2', views.actuator2view.as_view()),
    
    # Daging Merah 
    path('dagingputih/sensorkadarsodium', views.SensorKadarSodiumView.as_view()),
    path('dagingputih/sensorkadarprotein', views.SensorKadarProteinView.as_view()),
    path('dagingputih/sensorkadargula', views.SensorKadarGulaView.as_view()),
    path('actuator/actuator3', views.actuator3view.as_view()),

#Smart Plantation
    # Sumber Karbohidrat
    path('sensorkarbohidrat/kelembapantanah', views.SensorKelembapanTanahView.as_view()),
    path('sensorkarbohidrat/intensicahaya', views.SensorIntensiCahayaView.as_view()),
    path('sensorkarbohidrat/suhuudara', views.SensorSuhuUdaraView.as_view()),
    path('actuator/actuator4', views.actuator4view.as_view()),
    
    # Sayuran
    path('sayuran/suhutanah', views.SensorSuhuTanahView.as_view()),
    path('sayuran/sensorkelembapanudara', views.SensorKelembapanUdaraView.as_view()),
    path('sayuran/sensorkadarco2', views.SensorKadarCo2View.as_view()),
    path('actuator/actuator5', views.actuator5view.as_view()),
    
    # Buah-buahan
    path('buah/sensorkecepatanangin', views.KecepatanAnginView.as_view()),
    path('buah/sensorcurahhujan', views.CurahHujanView.as_view()),
    path('buah/sensorkualitasair', views.KualitasAirView.as_view()),
    path('actuator/actuator6', views.actuator6view.as_view()),

#Smart Restaurant
    # DeteKsi Musim
    path('musim/barometer', views.SensorBarometerView.as_view()),
    path('musim/ketebalanawan', views.SensorKetebalanAwanView.as_view()),
    path('musim/radiasisurya', views.SensorRadiasiSuryaView.as_view()),
    path('actuator/actuator7', views.actuator7view.as_view()),
    
    # Deteksi Hasil Penjualan Berfluktuasi
    path('hasilpenjualanberfluktuasi/cancelorder', views.SensorCancelOrderView.as_view()),
    path('hasilpenjualanberfluktuasi/penilaian', views.SensorPenilaianView.as_view()),
    path('hasilpenjualanberfluktuasi/jumlahpesanan', views.SensorJumlahPesananView.as_view()),
    path('actuator/actuator8', views.actuator8view.as_view()),
    
    # Deteksi Jumlah Pengunjung Restoran
    path('jumlahpengunjungrestoran/pendeteksigerakan', views.SensorPendeteksiGerakanView.as_view()),
    path('jumlahpengunjungrestoran/mejakosong', views.SensorMejaKosongView.as_view()),
    path('jumlahpengunjungrestoran/kebisingan', views.SensorKebisinganView.as_view()),
    path('actuator/actuator9', views.actuator9view.as_view()),

    path('actuator/actuatorsubsystem1', views.actuatorsubsystem1view.as_view()),
    path('actuator/actuatorsubsystem2', views.actuatorsubsystem2view.as_view()),
    path('actuator/actuatorsubsystem3', views.actuatorsubsystem3view.as_view()),
    path('actuator/actuatorsystem', views.actuatorsystemview.as_view())
]