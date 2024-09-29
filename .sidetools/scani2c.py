# Skrypt służący do odszukania adresów i2c urządzeń podłączonych przez ten protokół

# Iport modułów

from machine import Pin, SoftI2C

# Nadanie nazw funkcjonalnych odpowiednim pinom

led = Pin(8, Pin.OUT)
i2c_display_sda = 5
i2c_display_scl = 6


i2c = SoftI2C(sda=Pin(5), scl=Pin(6), freq = 400000)

def scan_i2c():
    devices = i2c.scan()
    
    if len(devices) == 0:
        print("No I2C devices found")
    else:
        print('Found I2C devices at addresses:')
        for device in devices:
            print(hex(device))

scan_i2c()

    