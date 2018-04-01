from . import accelerometer
import threading

# Just like accelerometer only thread safe
class accelerometerMT(accelerometer.accelerometer):
    """
    A class for reading data from the accelerometer sensor
    while keeping your program multithreading safe
    """

    def __init__(self):
        """
        Initialises the sensor object if the
        accelerometer is connected
        """
        
        accelerometer.accelerometer.__init__(self)
        self.lock = threading.Lock()

    def get_axes(self):
        """
        Measures acceleration in a form of a tuple containing
        x, y and z axis values while keeping your
        program multithreading safe
        """

        data = None
        with self.lock:
            data = self.__get_axes__()
        return data
