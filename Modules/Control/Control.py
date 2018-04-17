from ..Magnetometer import magnetometer_factory
from ..Magnetorquer import magnetorquerMT
from ..Gyro import gyro_factory
from ..Control import Scale_Convert
from threading import Thread
import math
import numpy
import time


__radius = 7370 * 1000
__circle_time = 90 * 60

class controller:
    def __init__(self,mode=1):
        self.magnetometer = magnetometer_factory.initialize()
        self.gyro = gyro_factory.initialize()
        self.magnetorquer = magnetorquerMT.magnetorquerMT()
        self.time = time.time()
        # Secondary thread that changes calls setControl
        thread = Thread(target = set_control, args = (2,))
        thread.start()
        thread.join()
	
    def move(self, mode = 2):
        while(True):
            arr = setControl(mode = mode)
            self.magnetorquer.set_x(arr[0])
            self.magnetorquer.set_y(arr[1])
            self.magnetorquer.set_z(arr[2])
            time.sleep(config.TIME_DIFFERENCE)
    #TODO: Add offset for meneuvering to certain locations on earth
    def set_control(self, mode=1, offset=[0,0]):
        if(mode == 1):
            field = self.magnetometer.get_axes()
            timer = (self.time-time.time()) % (90 * 60)
            torque = get_angle_vector(get_angle(timer))
            z = (field[1]*torque[0] - filed[0]*torque[1]) / (field[2]*torque[1] - field[1]*torque[2])
            y = (-field[0] - z * field[2]) / field[1]
            arr = np.ndarray([1,y,z])
            tilt = np.ndarray([self.gyro.accel()])
            return arr - tilt
        elif(mode == 2):
            # Makes the direction change for circular magnetic field, in order to go by the field
            return np.array([0,0,1])

''''
returns the ratio of y1 to x1 where (x1;y1) is the vertical 2D vector to (x;y) vector
'''
def two_demensions_vertical_vector(x:float,y:float):
    slowpe = x / y
    return -1 / slowpe

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

'''
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
        #This block is for depolar magnetic field
        #TODO : make this function take care of more than one half situations
        return math.degrees(math.acos(field.size))
    elif(mode == 2):
        #This block is for circular magnetic field
        a = field[0]
        b = field[1]
        y = math.sqrt(1 / (a**2 + b**2) )
        x = math.sqrt(a**2 / (a**2 * (a**2 + y**2))
        temp = math.sqrt(x**2/y**2 + 1)
        rad = math.acos(1 / temp)
        return math.degrees(rad) 