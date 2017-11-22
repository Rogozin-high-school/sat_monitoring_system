import random

class magnetometer:
    def __init__(this):
        ron = True

    def get_x(this):
        return random.randint(0,100)/100.0

    def get_y(this):
        return random.randint(0,100)/100.0

    def get_z(this):
        return random.randint(0,100)/100.0

    def get_axes(this):
        return (get_x() ,get_y() ,get_z())