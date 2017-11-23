import random

class magnetometer:
    def __init__(self):
        self.ron = True

    def get_x(self):
        return random.randint(0,100)/100.0

    def get_y(self):
        return random.randint(0,100)/100.0

    def get_z(self):
        return random.randint(0,100)/100.0

    def get_axes(self):
        return (self.get_x() ,self.get_y() ,self.get_z())