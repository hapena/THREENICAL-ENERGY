import network, time, urequests
from machine import Pin, ADC
from utime import sleep, sleep_ms

sensor_asc712 = ADC(Pin(34))
sensor_asc712.atten(ADC.ATTN_11DB)
sensor_asc712.width(ADC.WIDTH_10BIT)

sensibilidad = 0.185  # Puede variar según el modelo del sensor


def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True


if conectaWifi ("Wokwi-GUEST", ""):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url="https://api.thingspeak.com/update?api_key=P0RVEFGL9B1552F1"
    # ir a la siguiente URL para la visualización  https://thingspeak.com/channels/2154186

    while True:

        lectura_adc = sensor_asc712.read()
        # Convertir la lectura del ADC a corriente en amperios
        voltaje = (lectura_adc/ 1023) * 3.3
        
        corriente = (voltaje - 2.5)/sensibilidad
        print("Corriente: {:.2f} A , Voltaje: {:.2f} V".format(corriente, voltaje))
        
        respuesta = urequests.get(url+"&field1="+str(corriente)+"&field2="+str(voltaje))
        print(respuesta.text)
        print(respuesta.status_code)
        respuesta.close ()
        time.sleep(0.5)

 
else:
       print ("Imposible conectar")
       miRed.active (False)
