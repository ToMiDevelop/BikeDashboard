# Bike Dashboard

## 1. Brief introduction

In this repository you'll find the source code, custom PCB project, connection schmatics and custom cover designs of a simple digital dashboard.

## 2. Used components

- ESP32-C3 Super-Mini board
- LM2596 step-down voltage regulator
- limit switches
- DS18B20 temperature sensors
- 4 x 20 character display
- I2C converter for character display
- bi-directional 4 channel logic level converter
- 4.7 kOhm resitors
- some wires
- some pcb connectors
- PETG 3d printer filament

## 3. Brief source code description

The source code of the sripts running on the board are kept in the main path of the repo and in two folders: **lib** and **functions**. Main scripts runned on the board are: **boot.py** and **main.py**. All the folder and files, which need to be transfered to the board are visible on the tree bellow.

```
BikeDashboard
 |
 ├──────────── functions
 |              ├── display.py
 |              ├── temperature.py
 |              └── trunk.py
 |
 ├──────────── lib
 |              ├── i2c_lcd.py
 |              ├── lcd_api.py
 |              └── WIFI_CONFIG.py
 |
 ├── boot.py
 └── main.py
```

In the **boot.py** there is some initial configuarions and start on boot code. In the **main.py** there is code with the main logic of the application. In **lib** there are libraries used to talk with the display and a wifi configuration file, as the OTA updates are one of the project goals. In **functions** there are modules with classes used to invoke all the individualy tailored operations made on display, interactions with the temperature sensor and the limit switches.
