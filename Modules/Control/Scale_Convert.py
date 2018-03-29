import numpy

'''
Input:
    tilt - the tilt of the wanted scale in comparison to the given scale
    vector - the given vector for the first scale
Output:
    the given vector for the 2nd scale
'''
def convert(tilt:numpy.ndarray, vector:numpy.ndarray) -> numpy.ndarray:
    #this function converts between different scales for a known tilt
    return vector - tilt