from ..Field import circular_field
from ..Field import angle
import time
class fake_magnetometer:
    """Simulates a magnetometer sensor"""
    def __init__(self):
        self.start = time.time()
    def readMagnet(self):
        """ A dictionary with fake magnetomter values"""
        # Gets the location in the form of angle
        location = angle.get_angle(time.time() - self.start)
        # Gets the 2d vector for the 2d circular field
        vector = circular_field.circular_field(location)

        return {'x': vector[0], 'y': vector[1], 'z': 0.0}
