from gyro import gyro
import threading

class gyroMT(gyro):
    def __init__(self):
        gyro.__init__(self)
        self.lock = threading.Lock()
    def get_axis(self):
        data = None
        with self.lock:
            data = self.getAxis()
        return data