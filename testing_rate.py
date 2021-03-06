import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1015(i2c,data_rate=3300,mode=ADS.Mode.CONTINUOUS)

channel = AnalogIn(ads, ADS.P1) #1
val = []
xs_start = time.monotonic()
while len(val) < 3300:
    #print("{:>5}\t{:>5f}".format(channel.value, channel.voltage))
    val.append(channel.value)
    #xs.append(time.monotonic())
xs_end = time.monotonic()
print(xs_end-xs_start)
