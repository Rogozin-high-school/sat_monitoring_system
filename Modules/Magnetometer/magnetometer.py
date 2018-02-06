import random
import mpu9250

class magnetometer:
    def __init__(self):
        self.sensor = mpu9250.mpu9250()

    # Reading data from magnetometer
    # NOT MULTI THREADING SAFE
    # use magnetometerMT for that
    def __get_x__(self):
        return str(self.sensor.read_xyz()[0])

    def __get_y__(self):
        return  str(self.sensor.read_xyz()[1])

    def __get_z__(self):
        return str(self.sensor.read_xyz()[2])

    def __get_axes__(self):
        return self.sensor.read_xyz()