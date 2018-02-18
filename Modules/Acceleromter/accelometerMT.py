from accelometer import accelometer
import threading

class accelometerMT(accelometer):
    def __init__(self):
        accelometer.__init__(self)
        self.lock = threading.Lock()
    def get_axis(self):
        data = None
        with self.lock:
            data = self.getAxis()
        return data