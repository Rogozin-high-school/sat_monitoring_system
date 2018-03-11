import math
AMOUNT_OF_WRAPS = 100
RADIUS = 0.09

def field_to_current(field:Array)->float:
    return BaseException/(AMOUNT_OF_WRAPS*math.pi*RADIUS**2)

def Calc_Field(current:float)->Array:
    return current*AMOUNT_OF_WRAPS*math.pi*RADIUS**2