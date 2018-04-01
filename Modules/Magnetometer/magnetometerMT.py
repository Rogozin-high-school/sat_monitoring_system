from . import magnetometer
import threading

# Just like magnetometer only thread safe
class magnetometerMT(magnetometer.magnetometer):
    """
    A class for reading data from the magnetometer sensor
    while keeping your program multithreading safe
    """

    def __init__(self):
        """
        Initialises the sensor object if the
        magnetometer is connected
        """

        magnetometer.magnetometer.__init__(self)
        self.lock = threading.Lock()

    def get_axes(self):
        """
        Reads magnetic field in a form of a tuple containing
        x, y and z axis values while keeping your
        program multithreading safe
        """

        data = None
        with self.lock:
            data = self.__get_axes__()
        return data
