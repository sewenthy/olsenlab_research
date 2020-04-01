import time
import datetime
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1015(i2c,data_rate=3300,mode=ADS.Mode.CONTINUOUS)

channel = AnalogIn(ads, ADS.P1) #1

"""
Reads from the analog reader with timestamp--writing still takes time + time to call monotonic()
so will need around 1.8 seconds to write 1000 data points i.e ~550 sampling rate
"""
def writeValue():
    #count = 0
    with open("logs/Geophone_"+datetime.datetime.now().__str__()+".csv","w") as f:
        f.write("TIMESTAMP,RAW_VALUE,VOLTAGE\n")
        #start = time.monotonic()
        while 1:
            f.write("{},{:>5},{:>5f}\n".format(time.monotonic(),channel.value,channel.voltage))
            #count+=1
        #stop = time.monotonic()
    #print(stop-start)

"""
Reads from the analog reader but without using time stamp--writing still takes time
so will need around 1.4 seconds to write 1000 data points i.e ~700 sampling rate
"""
def writeValueNoTimestamp():
    #count = 0
    with open("logs/Geophone_"+datetime.datetime.now().__str__()+".csv","w") as f:
        f.write("RAW_VALUE,VOLTAGE\n")
        #start = time.monotonic()
        while 1:
            f.write("{:>5},{:>5f}\n".format(channel.value,channel.voltage))
            #count+=1
        #stop = time.monotonic()
    #print(stop-start)