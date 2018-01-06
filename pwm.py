import threading
import time
import supplier
class pwm:
    def __init__(self):
        self.val = 0
        self.lock = threading.Lock()
        self.timeSpan = 0.1
    def loop(self):
        while(True):
            percent = 0
            sign = 0
            with self.lock:
                percent = self.val
            if(percent>0):
                sign = 1
            else:
                sign = -1
            supplier.supply(sign)
            time.sleep(self.timeSpan*percent)
            supplier.supply(0)
            
