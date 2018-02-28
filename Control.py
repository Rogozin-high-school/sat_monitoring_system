from Modules.Magnetometer.magnetometerMT import magnetometerMT
import math


__radius = 7370 * 1000
__circle_time = 90 * 60
class controller:
    def __init__(self):
        self.magnetometer = magnetometerMT()
    def SetControl(self,mode=1):
        nothing = None

''''
returns the ratio of y1 to x1 where (x1;y1) is the vertical 2D vector to (x;y) vector
'''
def TwoDimensionsVerticalVector(x,y):
    slowpe = x/y
    return -1/slowpe

'''
parameters : time in seconds from measurment start
output : the angle of the satellite in comparison to earth
'''
def get_angle(time:int)->int:
    ratio = get_ratio(time)
    return ratio*360

'''
parameters : time in seconds from measurment start
output : the satellite location on the circle route around earth
'''
def get_location(time:int)->int:
    global __radius
    ratio = get_ratio(time)
    perimeter = 2 * math.pi * __radius
    return ratio*perimeter

'''
parameters : the time in seconds from measurments start
output : the ratio between the time passed and the circle time
'''
def get_ratio(time:int)->int:
    global __circle_time
    return (time % __circle_time) / __circle_time

