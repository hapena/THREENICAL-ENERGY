from machine import Pin
from utime import sleep

motorA1= Pin(13, Pin.OUT)
motorA2= Pin(12, Pin.OUT)

motorB1= Pin(27, Pin.OUT)
motorB2= Pin(14, Pin.OUT)


def adelante():
    print("adelante")
    motorA1.on()
    motorB1.on()
    motorA2.off()
    motorB2.off()

def atras():
    print("atras")
    motorA1.off()
    motorB1.off()
    motorA2.on()
    motorB2.on()

def derecha():
    motorA1.on()
    motorB1.off()
    motorA2.off()
    motorB2.off()

def izquierda():
    motorA1.off()
    motorB1.on()
    motorA2.off()
    motorB2.off()



while True:
    
     adelante()
     
     sleep(2)
     atras()
     sleep(2)
     

