from Modules.Magnetometer.magnetometerMT import magnetometerMT
from math import sqrt
class controller:
    def __init__(self):
        self.magnetometer = magnetometerMT()
    def SetControl(self,mode=1):
        nothing = None

# returns the ratio of y1 to x1 where (x1;y1) is the vertical 2D vector to (x;y) vector
def TwoDimensionsVerticalVector(x,y):
    slowpe = x/y
    return -1/slowpe

def TwoDimensionsVectorLength(x,y):
    return sqrt(x**2+y**2)

def ThreeDimesionsVectorLength(x,y,z):
    return sqrt(x**2+y**2+z**2) 

        
