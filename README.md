# Bike Dashboard

![Device prototype](/pics/prototype.jpg)

## 1. Brief repo description

In this repository you'll find the source code, custom PCB project, connection schmatics of a simple digital dashboard tailored for the bike of one of my friends.

## 2. Functionality and key principles

- The device is supposed to show live view of the engine's the outside world's temperature.
- The device shows also the state of 2 trunks - either if they are closed or open.
- The physical design has to enable the temperature sensors to be attached even more than 1 meter away from the microcontroller
- The lcd screen should be attached approx. 1.5 meters away from the microcontroller.
- Main electornics should be mounted in a custom 3d printed case bellow the seat.
- There is a need for a step-down voltage regulator to connect DIY equipment to the battery.

## 3. Used components

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

## 4. Brief source code description

The source code of the sripts running on the board are kept in the main path of the repo and in two folders: **lib** and **functions**. Main scripts runned on the board are: **boot.py** and **main.py**. All the folder and files, which need to be transfered to the microcontroller board are visible on the tree bellow.

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

## 5. Language notice
All of the interface is designed in Polish, you can freely customize it with the translation from **translations.json** file.

## 6. Other useful files

In **pics** you can find pictures of the custom made pcb and the working prototype. In **pcb** there are Gerber files of the the custom pcb board, renders of the board and z **zip** archive with the KiCad project. In the **.sidetools** forlder you'll find some small scripts I used to scan the one wire and i2c bus and to test the display.

## 7. Legal notice

I'm the only author of all the work covered in this repository. All the files made publicly available in ths reposotiry are licensed under the CC NY 4.0 license. The full licence text is available in **LICENSE** file.