from . import magnetorquer
import threading

class magnetorquerMT(magnetorquer.magnetorquer):
    def __init__(self):
        magnetorquer.magnetorquer.__init__(self)
        self.lock = threading.Lock()

    # Setters
    def set_x(self,x):
        with self.lock:
            self.__set_x__(x)

    def set_y(self,y):
        with self.lock:
            self.__set_y__(y)

    def set_z(self,z):
        with self.lock:
            self.__set_z__(z)

    # Getters
    def get_x(self):
        return_x = None
        with self.lock:
            return_x = self.__get_x__()
        return return_x
        
    def get_y(self):
        return_y = None
        with self.lock:
            return_y = self.__get_y__()
        return return_y

    def get_z(self):
        return_z = None
        with self.lock:
            return_z = self.__get_z__()
        return return_z
