import magnetorquer
import threading

class magnetorquer:
    def __init__(self):
        self.magnetorquer = magnetorquer.magnetorquer()
        self.lock = threading.lock()

    def update(self):
        with self.lock:
            # Update the magnetorquer according to the saved values
            self.implemented = False

    # Setters
    def set_x(self,x):
        with self.lock:
            self.x = x

    def set_y(self,y):
        with self.lock:
            self.y = y

    def set_z(self,z):
        with self.lock:
            self.z = z
    
    def set_axes(self,x,y,z):
        with self.lock:
            self.x = x
            self.y = y
            self.z = z

    # Getters
    def get_x(self):
        return_x = None
        with self.lock:
            return_x = self.get_x()
        return return_x
        
    def get_y(self):
        return_y = None
        with self.lock:
            return_y = self.get_y()
        return return_y

    def get_z(self):
        return_z = None
        with self.lock:
            return_z = self.get_z()
        return return_z

    def get_axes(self):
        return_axes = None
        with self.lock:
            return_axes = self.get_axes()
        return return_axes