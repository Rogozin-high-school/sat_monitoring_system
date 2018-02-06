import magnetometer
import threading

# Just like magnetometer only thread safe
class magnetometerMT(magnetometer.magnetometer):
    def __init__(self):
        magnetometer.magnetometer.__init__(self)
        self.lock = threading.Lock()

    def get_x(self):
        data = None
        with self.lock:
            data = self.__get_x__()
        return data

    def get_y(self):
        data = None
        with self.lock:
            data = self.__get_y__()
        return data

    def get_z(self):
        data = None
        with self.lock:
            data = self.__get_z__()
        return data

    def get_axes(self):
        data = None
        with self.lock:
            data = self.__get_axes__()
        return data