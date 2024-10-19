# Adding custom files to the path

import sys
import machine

sys.path.append('/lib')
sys.path.append('/functions')

# Creating a wifi connection

from WIFI_CONFIG import SSID, PASSWORD
import network

wlan = network.WLAN(network.WLAN.IF_STA) # type: ignore
wlan.active(True)
if not wlan.isconnected():
    print('Connecting to WiFi...')
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        pass
print('Connected to WiFi!')
print('IP v.4 adress:', wlan.ifconfig()[0])