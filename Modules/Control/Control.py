from ..Magnetometer import magnetometerMT
import math
import numpy
import time


__radius = 7370 * 1000
__circle_time = 90 * 60

class controller:
    def __init__(self, mode=1:int):
        self.magnetometer = magnetometerMT()
        self.time = time.time()
        #TODO : Add a secondary thread that changes calls setControl
        

    #TODO: Add offset for maneuvering to certain locations on earth
    def set_control(self, mode=1, offset=[0,0]):
        #makes the direction change for the measured circular magnetic field (cos function value)
        if(mode == 1):
            field = self.magnetometer.get_axes()
            timer = (self.time-time.time()) % (90*60)
            torque = get_angle_vector(get_angle(timer))
            z = (field[1]*torque[0] - filed[0]*torque[1]) / (field[2]*torque[1] - field[1]*torque[2])
            y = (-field[0] - z * field[2]) / field[1]
            return np.array([1,y,z])
		#TODO : add handling for bipolar field


''''
returns the ratio of y1 to x1 where (x1;y1) is the vertical 2D vector to (x;y) vector
'''
def two_demensions_vertical_vector(x:float,y:float):
    slowpe = x / y
    return -1 / slowpe

'''
parameters : time in seconds from measurement start
output : the angle of the satellite in comparison to earth
'''
def get_angle(time:int)->int:
    ratio = get_ratio(time)
    return ratio*360

'''
parameters : time in seconds from measurement start
output : the satellite location on the circle route around earth
'''
def get_location(time:int)->int:
    global __radius
    ratio = get_ratio(time)
    perimeter = 2 * math.pi * __radius
    return ratio*perimeter

'''
parameters : the time in seconds from measurements start
output : the ratio between the time passed and the circle time
'''
def get_ratio(time:int)->int:
    global __circle_time
    return (time % __circle_time) / __circle_time

'''
parameters : the angle of the satellite in comparison to the starting point
output : the vector of the satellite location from earth axis
changes angle to direction vector
'''
def get_angle_vector(angle:int)->numpy.ndarray:
    if((angle / 90) % 2 != 1):
        angle = math.radians(angle)
        x = 1
        value = 1 / (math.cos(angle) ** 2)
        z = math.sqrt(value-x)
        return numpy.array([x,0,z])
    else:
        if(angle == 90):
            return numpy.array([0,0,1])
        else:
            return numpy.array([0,0,-1])

#This function gets the satellite location (angle) by the measured  magnetic field
def get_angle_by_field(field:numpy.ndarray ,mode=1)->float:
    if(mode == 1):
        #This block is for circular magnetic field
        a = field[0]
        b = field[1]
        y = math.sqrt(1 / (a**2 + b**2) )
        x = math.sqrt(a**2 / (a**2 * (a**2 + y**2))
        temp = math.sqrt(x**2 / y**2 + 1)
        rad = math.acos(1 / temp)
        return math.degrees(rad) 
		#TODO : add block for bipolar field
		