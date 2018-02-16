#/usr/bin/python3
from math import sqrt
class vector2D:
    def __init__(self,x:float=0,y:float=0):
        self.x = x
        self.y = y
    def distanceTo(self,vector):
        return sqrt((self.x-vector.x)**2+(self.y-vector.y)**2)
    def length(self):
        return sqrt(self.x**2+self.y**2)
    def __add__(self,vector):
        return vector2D(self.x+vector.x,self.y+vector.y)