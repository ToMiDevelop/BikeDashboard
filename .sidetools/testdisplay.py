# Głóny skrypt kokpitu motorowego

# Iport modułów

from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import utime

# Nadanie nazw funkcjonalnych odpowiednim pinom

led = Pin(8, Pin.OUT)

i2c_display_sda = 5
i2c_display_scl = 6

# Określenie paramtrów wyświetlacza

i2c_display_adress = 0x27
i2c_display_rows = 4
i2c_display_columns = 20

# Określenie parametrów połączenia z wyświetlaczem

i2c_display_connection = SoftI2C(sda = Pin(i2c_display_sda), scl = Pin(i2c_display_scl), freq = 400000)

# Utworzenie obiektu reprezentującego wyświetlacz

display = I2cLcd(i2c = i2c_display_connection, i2c_addr= i2c_display_adress, num_lines = i2c_display_rows, num_columns = i2c_display_columns)

while True:
    display.move_to(0,0)
    display.putstr("Policzmy od 1 do 20!")
    utime.sleep(3)
    display.clear()
    display.move_to(0,0)
    display.putstr("Liczba:")
    for i in range(20):
        counted = str(i+1)
        if i+1 < 10:
            counted = '0' + counted
        display.move_to(0,2)
        display.putstr(counted)
        utime.sleep(1)
    display.clear()
