import numpy
import math
import time
from . import config

class fake_magnetometer:

    def __init__(self):
        pass

    #TODO : add real field simulation
    def read_xyz():
        return [0,0,0]

def circular_field(angle:float):

	angle = math.radians(angle)
	a = math.sin(angle)
	b = math.cos(angle)
	x = None
	y = None

	if(b > config.MIN_SIZE or b < -config.MIN_SIZE):
		x = 1
		y = -a/b
		length = math.sqrt(x**2 + y**2)
		x = x / length
		y = y / length
		return [x,y]
	else:
		x = 0
		y = a * FIELD_SIZES

	return [x,y]
