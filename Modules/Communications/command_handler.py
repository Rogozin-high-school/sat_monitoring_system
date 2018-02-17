from .Modules.Magnetometer import magnetometerMT

class command_handler:
    def __init__(self, magnetometer, magnetorquer, log, gyro, accelerometer)
        self.magnetometer = magnetometer
        self.magnetorquer = magnetorquer
        self.log = log
        self.gyro = gyro
        self.acceleromter = accelerometer

    def get_magnetometer(self, paramters):
        output += "'X':" + str(self.magnetometer.get_x()) + ","
        output += "'Y':" + str(self.magnetometer.get_y()) + ","
        output += "'Z':" + str(self.magnetometer.get_z())
        return output
