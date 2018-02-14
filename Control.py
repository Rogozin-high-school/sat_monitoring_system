from Modules.Magnetometer.magnetometerMT import magnetometerMT
class controller:
    def __init__(self):
        self.magnetometer = magnetometerMT()
    def SetControl(self,mode=1):
        