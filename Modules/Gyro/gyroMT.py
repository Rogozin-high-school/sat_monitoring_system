from . import gyro
import threading

# Just like gyro only thread safe
class gyroMT(gyro.gyro):
    """A class for reading data from the gyro sensor
    while keeping your program multithreading safe"""

    def __init__(self):
        """Initialises the sensor object if the
        gyro is connected"""
        gyro.gyro.__init__(self)
        self.lock = threading.Lock()

    def get_axes(self):
        """Reads gyro in a form of a tuple containing
        x, y and z axis values while keeping your
        program multithreading safe"""
        data = None
        with self.lock:
            data = self.__get_axes__()
        return data
