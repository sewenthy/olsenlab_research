import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

value_fig = plt.figure()
value_ax = fig.add_subplot(1,1,1)

voltage_fig = plt.figure()
voltage_ax = fig.add_subplot(1,1,1)

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1015(i2c)

channel = AnalogIn(ads, ADS.P0) #0

#print("{:>5}\t{:>5}".format('raw', 'v'))


def animate_value(i):
	xs = []
	values = []
	while len(values)<100:
		xs.append(time.monotonic())
	    values.append(channel.value)

    value_ax = clear()
    value_ax.plot(xs, values)

def animate_voltage(i):
	xs = []
	voltages = []
	while len(voltages)<100:
		xs.append(time.monotonic())
	    voltages.append(channel.voltage)

    voltage_ax = clear()
    voltage_ax.plot(xs, voltages)

ani_value = animation.FuncAnimation(value_fig,animate_value)
ani_voltage = animation.FuncAnimation(voltage_fig,animate_voltage)

plt.show()



