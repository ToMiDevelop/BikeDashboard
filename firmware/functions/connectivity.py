import utime
import network
from WIFI_CONFIG import SSID, PASSWORD
from i2c_lcd import I2cLcd


class Network:
    def networking(self):
        wlan = network.WLAN(network.WLAN.IF_STA) # type: ignore
        wlan.active(True)
        if not wlan.isconnected():
            start = utime.time()
            print('Łączenie z siecią WiFi...')
            self.display.move_to(0,3)
            self.display.putstr('[]')
            try:
                wlan.connect(SSID, PASSWORD)
                print('Połączono z WiFi!')
                print('Adres IP v.4 :', wlan.ifconfig()[0])
                while not wlan.isconnected():
                    elapsed = utime.time() - start
                    progress = int((elapsed / self.timeout) * 18)  # Progres na 18 znaków
                    middle = '=' * progress
                    bar = '[' + middle + ']'
                    self.display.move_to(0,3)
                    self.display.putstr(bar)
                    if elapsed >= self.timeout:
                        self.display.move_to(0,3)
                        self.display.putstr('[' + '=' * 18 + ']')
                        utime.sleep(0.5)
                        wlan.active(False)
                        return False
                if wlan.ifconfig()[0] == '0.0.0.0':
                    self.display.move_to(0,3)
                    self.display.putstr('[' + '=' * 18 + ']')
                    utime.sleep(0.5)
                    wlan.active(False)
                    return False
                else:
                    self.display.move_to(0,3)
                    self.display.putstr('[' + '=' * 18 + ']')
                    utime.sleep(0.5)
                    return True
            except:
                print('Brak połączenia z Wifi.')
                self.display.move_to(0,3)
                self.display.putstr('[' + '=' * 18 + ']')
                utime.sleep(0.5)
                wlan.active(False)
                return False
    def __init__(self, _display: I2cLcd, _timeout: int = 15):
        """
        This class is used to connect to WiFi and visualise the connection progress on the last line of the lcd as a progress bar.\n
        _display: a I2cLcd object from AppDisplay class - the display object\n
        _timeout: amount of seconds to wait for wstablishing the WiFi connection
        """
        self.timeout = _timeout
        self.display = _display
        self.IP = 'none'
        self.WiFiState = False
        self.WiFiState = self.networking()
        if self.WiFiState == True:
            self.IP = network.WLAN().ifconfig()[0]