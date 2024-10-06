# Main script file of the Bike's chockpit diplay

# Modules importing

from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
import utime

# Setting udeful names for chosen pin numbers and pin obejcts

led = Pin(8, Pin.OUT)

i2c_display_sda = 5
i2c_display_scl = 6

switch_1_nc = Pin(1, Pin.IN, Pin.PULL_DOWN)

switch_2_nc = Pin(4, Pin.IN, Pin.PULL_DOWN)

temp_sensor_pin = Pin(21, Pin.PULL_UP)

# Setting up the parameters of the display

i2c_display_adress = 0x27
i2c_display_rows = 4
i2c_display_columns = 20

# Initilizing the I2C connection to the display

i2c_display_connection = SoftI2C(sda = Pin(i2c_display_sda), scl = Pin(i2c_display_scl), freq = 400000)

# Initializing the object representing the lcd screen

display = I2cLcd(i2c = i2c_display_connection, i2c_addr= i2c_display_adress, num_lines = i2c_display_rows, num_columns = i2c_display_columns)

# Initializating of the object representing the temperature sensor

from temperature import Temperature
DSTemp = Temperature(temp_sensor_pin)

# Initilization of class responsible to comunicate with the limit switches

from trunk import Trunk
Trunks = Trunk(switch_1_nc, switch_2_nc)

# Initializing the object responsible to show infomration on the display

from display import Display
Show = Display(DSTemp, Trunks, i2c_display_sda, i2c_display_scl)

 # Showing boot screen and main menu frame

Show.EmptyScreen()
Show.BootScreen()
Show.MainMenu()

# Test of temperature readings, uncomment if desired

#Show.TemperatureOutside(True, -3.17)
#utime.sleep(6)
#Show.TemperatureOutside(True, -23.97)
#utime.sleep(6)
#Show.TemperatureOutside(True, 6.51)
#utime.sleep(6)
#Show.TemperatureOutside(True, 34.28)
#utime.sleep(6)

# Setting start point to count time interval to refresh temp (counted in seconds)

start = utime.time()

# Setting temp refrersh interval length (in seconds)

interval = 60

# Initial temperature display

Show.TemperatureOutside()

# Main app loop continuosly refreshing the temperature and trunks state

while True:
    Show.TrunksState()
    end = utime.time()
    if end - start >= interval:
        # Sprawdzenie i wyświetlenie temperatury
        Show.TemperatureOutside()
        start = end