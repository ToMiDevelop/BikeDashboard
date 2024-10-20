# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()


# Importing standard modules

import sys

# Importing WiFi connection data

# from WIFI_CONFIG import SSID, PASSWORD

# Adding extra folders to system path

sys.path.append('/lib')
sys.path.append('/functions')

print('Rozruch systemu rozpoczęty!')

# Creating a wifi connection and showing a screen if succeeded

# def networking():
#    wlan = network.WLAN(network.WLAN.IF_STA) # type: ignore
#    wlan.active(True)
#    if not wlan.isconnected():
#        print('Connecting to WiFi...')
#        wlan.connect(SSID, PASSWORD)
#        while not wlan.isconnected():
#            pass
#    if wlan.isconnected():
#        print('Connected to WiFi!')
#        print('IP v.4 adress:', wlan.ifconfig()[0])