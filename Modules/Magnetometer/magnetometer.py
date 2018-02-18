from . import config

if config.MAGNETOMETER_CONNECTED:
    from . import mpu9250

class magnetometer:
    """A class for reading data from the magnetometer sensor"""

    def __init__(self):
        """Initialises the sensor object if the
        magnetometer is connected"""
        if config.MAGNETOMETER_CONNECTED:
            self.sensor = mpu9250.mpu9250()

    # Reading data from magnetometer
    # NOT MULTI THREADING SAFE
    # use magnetometerMT for that
    def __get_x__(self):
        """Reads x axis magnetic field value"""
        return str(self.__get_axes__()[0])

    def __get_y__(self):
        """Reads y axis magnetic field value"""
        return str(self.__get_axes__()[1])

    def __get_z__(self):
        """Reads z axis magnetic field value"""
        return str(self.__get_axes__()[2])

    def __get_axes__(self):
        """Reads magnetic field in a form of a tuple containing
        x, y and z axis values"""
        if config.MAGNETOMETER_CONNECTED:
            return self.sensor.read_xyz()
        else:
            return (0,0,0)        
