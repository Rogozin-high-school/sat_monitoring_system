from .. import config

if config.MAGNETOMETER_CONNECTED:
    from . import mpu9250

class accelerometer:
    """A class for reading data from the accelerometer sensor"""

    def __init__(self):
        """Initialises the sensor object if the
        accelerometer is connected"""
        if config.MAGNETOMETER_CONNECTED:
            self.sensor = mpu9250.mpu9250()

    # Reading data from accelerometer
    # NOT MULTI THREADING SAFE
    # use accelerometerMT for that
    def __get_x__(self):
        """Measures x axis acceleration value"""
        return str(self.__get_axes__()[0])

    def __get_y__(self):
        """Measures y axis acceleration value"""
        return str(self.__get_axes__()[1])

    def __get_z__(self):
        """Measures z axis acceleration value"""
        return str(self.__get_axes__()[2])

    def __get_axes__(self):
        """Measure acceleration in a form of a tuple containing
        x, y and z axis values"""
        if config.MAGNETOMETER_CONNECTED:
            return self.sensor.read_xyz()
        else:
            return (0,0,0)        