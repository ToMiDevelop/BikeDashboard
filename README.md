# Bike Dashboard

|Prototype|Boot screen|
|-|-|
![Device prototype](/pics/prototype.jpg)|![Device prototype](/pics/boot_screen.jpg)|

|Main menu|Left trunk closed, right trunk open|
|-|-|
![Device prototype](/pics/main_screen.jpg)|![Device prototype](/pics/l_closed_r_open.jpg)|

|Temperature sensors calibration screen|Fully functional main screen|
|-|-|
![Device prototype](/pics/calibration_screen.jpg)|![Device prototype](/pics/main_screen_full.jpg)|

|PCB - soldered bottom|PCB - soldered top|
|-|-|
![Device prototype](/pics/pcb_bottom_soldered.jpg)|![Device prototype](/pics/pcb_soldered_top.jpg)|

## 1. Brief repo description

In this repository you'll find the source code, custom PCB project, connection schematics of a simple digital dashboard tailored for the bike of one of my friends.

## 2. Functionality and key principles

- The device is supposed to show live view of the engine's the outside world's temperature.
- The device shows also the state of 2 trunks - either if they are closed or open.
- The physical design has to enable the temperature sensors to be attached even more than 1 meter away from the microcontroller
- The lcd screen should be attached approx. 1.5 meters away from the microcontroller.
- Main electronics should be mounted in a custom 3d printed case bellow the seat.
- There is a need for a step-down voltage regulator to connect DIY equipment to the battery.

## 3. Used components

- [ESP32-C3 Super-Mini board](https://pl.aliexpress.com/item/1005006096717048.html?src=bing&aff_short_key=UneMJZVf&aff_platform=true&isdl=y&albch=shopping&acnt=135095331&isdl=y&albcp=554979198&albag=1310619002143550&slnk=&trgt=pla-4585513252290472&plac=&crea=81913742884006&netw=o&device=c&mtctp=e&utm_source=Bing&utm_medium=shopping&utm_campaign=PA_Bing_PLA_PL_PC_SFFC_0-7_20240613&utm_content=0-7&utm_term=esp32%20c3%20super%20mini%20amazon&msclkid=571fcd1d5eb315ebd46eaa1f84995cf0&gatewayAdapt=glo2pol)
- [LM2596 step-down voltage regulator](https://botland.com.pl/przetwornice-step-down/4871-przetwornica-step-down-lm2596-32v-35v-3a-z-wyswietlaczem-5904422359560.html)
- [limit switches](https://botland.com.pl/czujniki-krancowe/919-wylacznik-czujnik-krancowy-mini-z-rolka-wk625-5szt-5904422372958.html)
- [DS18B20 temperature sensors](https://botland.com.pl/sondy-wodoodporne/19516-sonda-wodoodporna-z-czujnikiem-temperatury-ds18b20-sent0002-2m-5904422307073.html)
- [4 x 20 character display](https://botland.com.pl/wyswietlacze-alfanumeryczne-i-graficzne/19734-wyswietlacz-lcd-4x20-znakow-niebieski-justpi-5903351243100.html?cd=518903701&ad=1317217320011988&kd=&msclkid=fb46d02c473e1ffb539ab72e9be8244d&utm_source=bing&utm_medium=cpc&utm_campaign=PLA%20-%20elektronika%20-%2006.2023&utm_term=2334125747398059&utm_content=Ad%20group%20%231)
- [I2C converter for character display](https://botland.com.pl/konwertery-pozostale/2352-konwerter-i2c-dla-wyswietlacza-lcd-hd44780-5903351248693.html)
- [bi-directional 4 channel logic level converter](https://botland.com.pl/konwertery-napiec/2259-konwerter-poziomow-logicznych-dwukierunkowy-4-kanalowy-sparkfun-bob-12009-5903351248716.html)
- [4.7 kOhm resistors](https://botland.com.pl/rezystory-przewlekane/20152-rezystor-justpi-tht-cf-weglowy-14w-47k-30szt-5904422329303.html)
- some wires
- some pcb connectors
- PETG 3d printer filament

## 4. Brief source code description

The source code of the scripts running on the board is kept in the **firmware** folder residing in main path of the repository. It contains two subfolders: **lib** and **functions**. Main scripts executed on the board are: **boot.py** and **main.py**. All the folder and files, which need to be transferred to the microcontroller board are visible on the tree bellow.

```
firmware
│
├──── functions
│     ├── display.py
│     ├── temperature.py
│     └── trunk.py
│
├──── lib
│     ├── i2c_lcd.py
│     ├── lcd_api.py
│     └── WIFI_CONFIG.py
│
├── boot.py
└── main.py
```

In the **boot.py** there is some initial configurations and start on boot code. In the **main.py** there is code with the main logic of the application. In **lib** there are libraries used to talk with the display and a wifi configuration file, as the OTA updates are one of the project goals. In **functions** there are modules with classes used to invoke all the individually tailored operations made on display, interactions with the temperature sensor and the limit switches.

## 6. Custom PCB Board

In this project I'm using a custom designed PCB board. All the design files can be found in the **pcb** folder.

```
pcb
│
├──── gerber                            
│     ├── Kokpit Final-B_Cu.gbr        
│     ├── Kokpit Final-B_Mask.gbr       
│     ├── Kokpit Final-B_Paste.gbr  
│     ├── Kokpit Final-B_Silkscreen.gbr
│     ├── Kokpit Final-Edge_Cuts.gbr
│     ├── Kokpit Final-F_Cu.gbr        
│     ├── Kokpit Final-F_Mask.gbr       
│     ├── Kokpit Final-F_Paste.gbr  
│     ├── Kokpit Final-F_Silkscreen.gbr
│     ├── Kokpit Final-job.gbrjob
│     ├── Kokpit Final-NPTH.drl
│     └── Kokpit Final-PTH.drl
│
├──── renders                           
│     ├── Back.png
│     └── Front.png
│
└── BikeDashboard_KiCad.zip

```
In **gerber** folder there are all the generated gerber files. The **BikeDashboard_KiCad.zip** is a export of the whole KiCad project.

|PCB - front render|PCB - back render|
|-|-|
|![Device prototype](/pcb/renders/Front.png)|![Device prototype](/pcb/renders/Back.png)|

## 5. Language notice

All of the interface is designed in Polish, you can freely customize it with the translation from **translations.json** file.

## 7. Minor side tools

In the **.sidetools** folder you'll find some small scripts I used to scan the one wire and i2c bus and to test the display.

## 8. Legal notice

I'm the only author of all the work covered in this repository. All the files made publicly available in the repository are licensed under the BikeDasboard project license. The full licence text is available in **LICENSE** file.