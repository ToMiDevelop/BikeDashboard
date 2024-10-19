from machine import Pin
import onewire, ds18x20

class Temperature:
    def __init__(self, _temp_outside_pin: Pin):
        """
        This class initializes the connection between the DS18B20 sensors and the board and provides functions
        to read the temperature from a chosen sensor.\n
        At the moment only one sensor is implemented. At the moment of initialization of the class object onewirebus is
        scanned for the device adresses and the one with index 0 is used.\n
        _temp_outside_pin - machine Pin attacked to the sensor, pin number only and pull up option specified
        """
        self.outside_temp_sensor_pin = _temp_outside_pin
        self.ds_sensors_outside = ds18x20.DS18X20(onewire.OneWire(self.outside_temp_sensor_pin))
        self.temp_sensor_outside_addr = self.ds_sensors_outside.scan()[0]
    def Temp_outside(self, _test: bool = False, _testing_temp: float = 0.00):
        """
        Calling this function wothout arguments returns the temperature whis is read from the ouside
        temperature sensor.\n
        Calling this function with _test = True provides a test to display different temepratures, positive, negative,
        and also from [-9.99 , 9.99] interval. If you want to perform a test please provide also the temperature value
        to be displayed as float in _testing_temp argument.\n
        The value returned is a string, rounded to 2 decimal places after the separator.\n
        _test: bool with default False value\n
        _testing_temp: float with default 0.00 value
        """
        if _test == False:
            temp_to_display = ''
            self.ds_sensors_outside.convert_temp()
            tempC = self.ds_sensors_outside.read_temp(self.temp_sensor_outside_addr)
            if tempC >= 10:
                temp_to_display = str(round(tempC,2))
            if tempC <= 0 and tempC < 10:
                temp_to_display = ' ' + str(round(tempC,2))
            if tempC > -10 and tempC < 0:
                temp_to_display = str(round(tempC,2))
            if tempC <= -10:
                temp_to_display = '-' + str(round(tempC,1))
            return(temp_to_display)
        else:
            temp_to_display = ''
            tempC = _testing_temp
            if tempC >= 10:
                temp_to_display = str(round(tempC,2))
            if tempC >= 0 and tempC < 10:
                temp_to_display = ' ' + str(round(tempC,2))
            if tempC > -10 and tempC < 0:
                temp_to_display = str(round(tempC,2))
            if tempC <= -10:
                temp_to_display = str(round(tempC,1))
            return(temp_to_display)