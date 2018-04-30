import math

from . import config

'''
Input - the location of the satellite in the form of angle
Output - 2 dimensional field that represents the field for the given angle
'''
def circular_field(angle:float):

	angle = math.radians(angle)
	a = math.sin(angle)
	b = math.cos(angle)
	x = None
	y = None

	if(b > config.MIN_SIZE or b < -config.MIN_SIZE):
		x = 1 * (b / abs(b))
		y = -a/b
		length = math.sqrt(x**2 + y**2)
		x = (x / length) * config.FIELD_SIZE
		y = (y / length) * config.FIELD_SIZE
		return (x ,y)
	else:
		x = 0
		y = -a * config.FIELD_SIZE

	return (x ,y)
