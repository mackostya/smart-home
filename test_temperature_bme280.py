#!/usr/bin/env python

import time
from bmp280 import BMP280

try:
       from smbus2 import SMBus
except ImportError:
       from smbus import SMBus

print("""temperature-and-pressure.py - Displays the temperature and pressure.

Press Ctrl+C to exit!

""")

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

while True:
          temperature = bmp280.get_temperature()
          pressure = bmp280.get_pressure()
          degree_sign = u"\N{DEGREE SIGN}"
          format_temp = "{:.2f}".format(temperature)
          print('Temperature = ' + format_temp + degree_sign + 'C')
          format_press = "{:.2f}".format(pressure)
          print('Pressure = ' + format_press + ' hPa \n')
          time.sleep(4)