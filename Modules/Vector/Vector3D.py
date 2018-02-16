#/usr/bin/python3
from math import sqrt
class vector3D:
    def __init__(self,x:float=0,y:float=0,z:float=0):
        self.x = x
        self.y = y
        self.z = z
    def distanceTo(self,vector)->int:
        return sqrt((self.x-vector.x)**2+(self.y-vector.y)**2+(self.z-vector.z)**2)
    def length(self)->int:
        return sqrt(self.x**2+self.y**2+self.z**2)
    def __add__(self,vector):
        return vector3D(self.x+vector.x,self.y+vector.y,self.z+vector.z)