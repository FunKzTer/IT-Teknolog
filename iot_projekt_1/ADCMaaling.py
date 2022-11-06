import umqtt_robust2 as mqtt
from machine import Pin,ADC
from time import sleep
import tm1637
import _thread

analog_pin = ADC(Pin(34))
analog_pin.atten(ADC.ATTN_11DB)
analog_pin.width(ADC.WIDTH_12BIT)

tm = tm1637.TM1637(clk=Pin(2), dio=Pin(4))

def batteri_maaling():
    while True:
        analog_val = analog_pin.read()
        volts = (analog_val * 0.00094545)*5
        battery_percentage = volts*100 - 320
        realBattery = battery_percentage / 2
        
        tm.number(int(realBattery))
        
        #print("The Battery percentage is:", battery_percentage / 2,"%")
        mqtt.web_print(battery_percentage / 2, 'Andersschiller/feeds/IoTFeed/csv') #IoTFeed udskiftes til det feed man skal bruge
        sleep(5)

_thread.start_new_thread(batteri_maaling,())