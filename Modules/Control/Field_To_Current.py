import math
AMOUNT_OF_WRAPS = 100
RADIUS = 0.09

def Field_To_Current(field):
    return BaseException/(AMOUNT_OF_WRAPS*math.pi*RADIUS**2)

def Calc_Field(current):
    return current*AMOUNT_OF_WRAPS*math.pi*RADIUS**2