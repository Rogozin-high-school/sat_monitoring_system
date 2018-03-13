from . import config

if config.GYRO_CONNECTED:
    from . import mpu9250

class gyro:
    """A class for reading data from the gyro sensor"""

    def __init__(self):
        """Initialises the sensor object if the
        gyro is connected"""
        if config.GYRO_CONNECTED:
            self.sensor = mpu9250.mpu9250()

    # Reading data from gyro
    # NOT MULTI THREADING SAFE
    # use gyroMT for that
    def __get_x__(self):
        """Reads x axis gyro value"""
        return str(self.__get_axes__()[0])

    def __get_y__(self):
        """Reads y axis gyro value"""
        return str(self.__get_axes__()[1])

    def __get_z__(self):
        """Reads z axis gyro value"""
        return str(self.__get_axes__()[2])

    def __get_axes__(self):
        """Reads gyro in a form of a tuple containing
        x, y and z axis values"""
        if config.GYRO_CONNECTED:
            return self.sensor.gyro()
        else:
            return (0,0,0)
			
