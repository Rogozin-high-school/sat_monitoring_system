from mpu9250 import mpu9250

class accelometer:
    def __init__(self):
        self.sensor = mpu9250()
    def getAxis(self):
        return self.sensor.accel()