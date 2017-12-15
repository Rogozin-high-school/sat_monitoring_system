import magnetometer
import threading

# Just like magnetometer only thread safe
class magnetometerMT(magnetometer.magnetometer):
    def __init__(self):
        magnetometer.magnetometer.__init__(self)
        self.lock = threading.Lock()

    def x(self):
        data = None
        with self.lock:
            data = self.get_x()
        return data

    def y(self):
        data = None
        with self.lock:
            data = self.get_y()
        return data

    def z(self):
        data = None
        with self.lock:
            data = self.get_z()
        return data

    def axes(self):
        data = None
        with self.lock:
            data = self.get_axes()
        return data