#/usr/bin/python3
from math import sqrt
class Vector3D:
    def __init__(self,x:float,y:float,z:float):
        self.x = x
        self.y = y
        self.z = z
    def DistanceTo(self,vector)->int:
        return sqrt((self.x-vector.x)**2+(self.y-vector.y)**2+(self.z-vector.z)**2)
    def Length(self)->int:
        return sqrt(self.x**2+self.y**2+self.z**2)