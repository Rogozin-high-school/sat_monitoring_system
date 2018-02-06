import random
from mpu9250.mpu9250 import mpu9250

class magnetometer:
    def __init__(self):
        self.ron = True
        self.sensor = mpu9250()


    # ALL OF THESE METHODS SHOULD NOT BE USED ANYWHERE
    # EXCEPT FOR THE magnetomterMT CLASS !!!
    def __get_x__(self):
        return str(self.sensor.read_xyz()[0])

    def __get_y__(self):
        return  str(self.sensor.read_xyz()[1])

    def __get_z__(self):
        return str(self.sensor.read_xyz()[2])

    def __get_axes__(self):
        return self.sensor.read_xyz()