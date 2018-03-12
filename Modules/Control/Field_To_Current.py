import math
import numpy
AMOUNT_OF_WRAPS = 100
RADIUS = 0.09 #(meter)
RESISTANCE = 170 #(ohm)

def field_to_current(field:numpy.ndarray)->float:
    return field / (AMOUNT_OF_WRAPS * math.pi * RADIUS**2)

def calc_field(current:float)->float:
    return current * AMOUNT_OF_WRAPS * math.pi * RADIUS**2

def current_to_voltage(current:float)->float:
    return current*RESISTANCE

def voltage_to_current(voltage:float)->float:
    reutrn voltage/RESISTANCE