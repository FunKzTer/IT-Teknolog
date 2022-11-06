import tm1637 
from imu import MPU6050
import time
from machine import Pin, I2C
import _thread

i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
imu = MPU6050(i2c)

tm1 = tm1637.TM1637(clk=Pin(13), dio=Pin(14))


def tacklet():
    antal_fald = 0
    acceleration = imu.accel
    tackled = False
    while True:
        
        if tackled == False and abs(acceleration.x) > 0.8:
            tackled = True
            #print("Spiller er opper og stå igen")
            
        elif tackled == True and acceleration.x < 0:
            #print("Spiller er blevet tacklet!")
            tackled = False
            antal_fald = antal_fald +1
        
        tm1.number(antal_fald)
        
        
        #print("acceleration.x", acceleration.x)
        #print("antal fald", antal_fald)
        
        time.sleep(5)

_thread.start_new_thread(tacklet,())

