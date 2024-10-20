# Main script file of the Bike's chockpit diplay

# setting app version
version = '0.5'

# Modules importing

from machine import Pin #, SoftI2C
#from i2c_lcd import I2cLcd
import utime

# Setting udeful names for chosen pin numbers and pin obejcts

led = Pin(8, Pin.OUT)

i2c_display_sda = 4
i2c_display_scl = 3

switch_lef_nc = Pin(7, Pin.IN, Pin.PULL_DOWN)
switch_right_nc = Pin(21, Pin.IN, Pin.PULL_DOWN)

temp_sensor_pin_external = Pin(0, Pin.PULL_UP)
temp_sensor_pin_engine = Pin(1, Pin.PULL_UP)

# Setting up the parameters of the display

i2c_display_adress = 0x27
i2c_display_rows = 4
i2c_display_columns = 20

# Initilizing the I2C connection to the display

#i2c_display_connection = SoftI2C(sda = Pin(i2c_display_sda), scl = Pin(i2c_display_scl), freq = 400000)

# Initializing the object representing the lcd screen

#display = I2cLcd(i2c = i2c_display_connection, i2c_addr= i2c_display_adress, num_lines = i2c_display_rows, num_columns = i2c_display_columns)

# Initializating of the object representing the temperature sensor

from temperature import Temperature
DSTemp_external = Temperature(temp_sensor_pin_external)
DSTemp_engine = Temperature(temp_sensor_pin_engine)

# Initilization of class responsible to comunicate with the limit switches

from trunk import Trunk
Trunks = Trunk(switch_lef_nc, switch_right_nc)

# Initializing the object responsible to show information on the display

from display import AppDisplay
Show = AppDisplay(DSTemp_external, DSTemp_engine, Trunks, i2c_display_sda, i2c_display_scl)


# Creating WiFi object representing the WiFi network connection and it's state

from WIFI_CONFIG import SSID
from connectivity import Network

 # Showing boot and diagnostic screens, connecting to WiFi

Show.BootScreen(version)
WiFi = Network(Show.display, 10)
if WiFi.WiFiState == True:
    Show.WifiScreen(SSID, WiFi.IP)
    import OTAtest
    OTAtest.Test()
if WiFi.WiFiState == False:
    Show.NoWifiScreen()
Show.CalibrateScreen()
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
        Show.TemperatureEngine()
        start = end