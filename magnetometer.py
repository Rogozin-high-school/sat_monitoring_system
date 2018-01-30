import random
from mpu9250.mpu9250 import mpu9250

class magnetometer:
    def __init__(self):
        self.ron = True
        self.sensor = mpu9250()


    # ALL OF THESE METHODS SHOULD NOT BE USED ANYWHERE
    # EXCEPT FOR THE magnetomterMT CLASS !!!
    def get_x(self):
        return str(self.sensor.read_xyz()[0])

    def get_y(self):
        return  str(self.sensor.read_xyz()[1])

    def get_z(self):
        return str(self.sensor.read_xyz()[2])

    def get_axes(self):
        return self.sensor.read_xyz()