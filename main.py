from machine import Pin
import utime

trigger = Pin(1, Pin.OUT)
echo = Pin(0, Pin.IN)
green = Pin(2, Pin.OUT)
yellow = Pin(3, Pin.OUT)
red = Pin(4, Pin.OUT)

def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    
    if distance >= 0 and distance <= 10:
        green.value(0)
        yellow.value(0)
        red.value(1)
    elif distance <= 30 and distance > 10:
        green.value(0)
        yellow.value(1)
        red.value(0)
    else:
        green.value(1)
        yellow.value(0)
        red.value(0)

while True:
    ultra()
    utime.sleep(1)
