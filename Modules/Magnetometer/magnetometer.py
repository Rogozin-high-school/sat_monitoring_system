from .. import config

if not config.HAS_HARDWARE:
    from . import mpu9250
else:
    import random

class magnetometer:
    def __init__(self):
        if not config.HAS_HARDWARE:
            self.sensor = mpu9250.mpu9250()

    # Reading data from magnetometer
    # NOT MULTI THREADING SAFE
    # use magnetometerMT for that
    def __get_x__(self):
        return str(self.__get_axes__()[0])

    def __get_y__(self):
        return str(self.__get_axes__()[1])

    def __get_z__(self):
        return str(self.__get_axes__()[2])

    def __get_axes__(self):
        if not config.HAS_HARDWARE:
            return self.sensor.read_xyz()
        else:
            return (0,0,0)        
