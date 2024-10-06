from machine import Pin, SoftI2C
import utime
#from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from temperature import Temperature
from trunk import Trunk

class Display:
    def __init__(self,
                 _temp_sensors: Temperature,
                 _trunks: Trunk,
                 _i2c_display_sda: int,
                 _i2c_display_scl: int,
                 _i2c_display_adress: int = 0x27,
                 _i2c_display_rows: int = 4,
                 _i2c_display_columns: int = 20):
        """
        This class establishes the connection with an i2c charcter display and provides functions used to
        display the boor scrren, main menu and refresh parts of the screen - temperature
        and state of the trunks lids.\n
        _temp_sensors: instance of Temperature class from temperature module\n
        _trunks: instance of Trunk class from trunk module\n
        _i2c_display_adress: connected i2c display adress, default = 0x27\n
        _i2c_display_sda: int number of pin connected to sda of i2c display\n
        _i2c_display_scl: int number of pin connected to scl of i2c display\n
        _i2c_display_rows: int number of i2c display rows, default = 4\n
        _i2c_display_columns: int number of i2c display rows, default = 20\n
        """
        self.temp_sensors = _temp_sensors
        self.trunks = _trunks
        self.i2c_display_sda = _i2c_display_sda
        self.i2c_display_scl = _i2c_display_scl
        self.i2c_display_adress = _i2c_display_adress
        self.i2c_display_rows = _i2c_display_rows
        self.i2c_display_columns = _i2c_display_columns
        self.i2c_display_connection = SoftI2C(sda = Pin(self.i2c_display_sda),
                                              scl = Pin(self.i2c_display_scl),
                                              freq = 400000)
        self.display = I2cLcd(i2c = self.i2c_display_connection,
                              i2c_addr= self.i2c_display_adress,
                              num_lines = self.i2c_display_rows,
                              num_columns = self.i2c_display_columns)
    def BootScreen(self):
        """
        This function shows the boot screen. Called without arguments.
        """
        self.display.clear()
        self.display.move_to(2,0)
        self.display.putstr('Motocykl Piotrka')
        utime.sleep(0.5)
        self.display.move_to(5,1)
        self.display.putstr('wersja 0.3')
        utime.sleep(0.5)
        self.display.move_to(0,2)
        self.display.putstr('uruchamianie systemu')
        utime.sleep(0.5)
        for i in range(19):
            middle = '-' * i
            bar = '<' + middle + '>'
            self.display.move_to(0,3)
            self.display.putstr(bar)
            utime.sleep(0.1)
        utime.sleep(1.5)
    def MainMenu(self):
        """
        This functions is used to display the main menu frame. Called without arguments.
        """
        self.display.clear()
        self.display.move_to(1,0)
        self.display.putstr('Zewn.:') # wyswuetlanie temperatury na 8,0 zaokrąglenie do 2 cyf # wyswietlanie koncówki 'st. C' na pozycji 14,0
        self.display.move_to(14,0)
        self.display.putstr('st. C')
        self.display.move_to(1,1)
        self.display.putstr('Siln.: --.--') # wyswuetlanie temperatury na 8,0 zaokrąglenie do 2 cyf # wyswietlanie koncówki 'st. C' na pozycji 14,0
        self.display.move_to(14,1)
        self.display.putstr('st. C')
        # -Kufer L----Kufer P-
        # -OTWARTY----OTWARTY-
        # --ZAMK.------ZAMK.--
        # -!!!!!!!----!!!!!!!-
        # -       ----       -
        self.display.move_to(0,2)
        self.display.putstr(' Kufer L    Kufer P')
        utime.sleep(1)
        # Sprawdzenie i pierwsze wyświetlenie temperatury
        self.display.move_to(8,0)
        self.display.putstr(self.temp_sensors.Temp_outside())
        print('Temperatura: ' + self.temp_sensors.Temp_outside())
        print('Lewy kufer:', self.trunks.TrunkState())
        print('Prawy kufer:', self.trunks.TrunkState('right'))
    def TrunksState(self):
        """
        This function is used to refersh and display trunks state in main app loop. Called without arguments.
        """
        self.display.move_to(1,3)
        self.display.putstr(self.trunks.TrunkState())
        self.display.move_to(12,3)
        self.display.putstr(self.trunks.TrunkState('right'))
    def TemperatureOutside(self, _test: bool = False, _testing_temp: float = 0.00):
        """
        This function is used to get and show the outside temperature. Called without arguments.\n
        Calling this function with _test = True provides a test to display different temepratures, positive, negative,
        and also from [-9.99 , 9.99] interval. If you want to perform a test please provide also the temperature value
        to be displayed as float in _testing_temp argument.\n
        _test: bool with default False value\n
        _testing_temp: float with default 0.00 value
        """
        if _test == False:
            self.display.move_to(8,0)
            self.display.putstr(self.temp_sensors.Temp_outside())
            print('Temperatura: ' + self.temp_sensors.Temp_outside())
            print('Lewy kufer:', self.trunks.TrunkState())
            print('Prawy kufer:', self.trunks.TrunkState('right'))
        else:
            self.display.move_to(8,0)
            self.display.putstr(self.temp_sensors.Temp_outside(True, _testing_temp))
            print('Temperatura: ' + self.temp_sensors.Temp_outside())
            print('Lewy kufer:', self.trunks.TrunkState())
            print('Prawy kufer:', self.trunks.TrunkState('right'))
    def EmptyScreen(self):
        """
        This function is used to clear the screen. Called without arguments.
        """
        self.display.clear()