import math
import numpy
import config as c

def field_to_current(field:numpy.ndarray)->float:
    return field / (c.AMOUNT_OF_WRAPS * math.pi * c.RADIUS**2)

def calc_field(current:float)->float:
    return current * c.AMOUNT_OF_WRAPS * math.pi * c.RADIUS**2

def current_to_voltage(current:float)->float:
    return current * c.RESISTANCE

def voltage_to_current(voltage:float)->float:
    reutrn voltage / c.RESISTANCE