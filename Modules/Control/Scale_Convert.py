import numpy

def convert(tilt:numpy.ndarray ,target:numpy.ndarray) ->numpy.ndarray:
    #this function converts between different scales for a known tilt
    x = target[0]-tilt[0]
    y = target[1] - tilt[1]
    z = target[2] - tilt[2]
    return numpy.ndarray([x,y,z])