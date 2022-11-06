from time import sleep
import time
import umqtt_robust2 as mqtt
import _thread
import ADCMaaling
import Tackling
import GPSCalculation
import gps_funktion
_thread.start_new_thread(gps_funktion.gps_main, ())


        
while True:
    try:
        sleep(5)
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""            
            mqtt.syncWithAdafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        print(".", end = '') # printer et punktum til shell, uden et enter        
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit() 
    
