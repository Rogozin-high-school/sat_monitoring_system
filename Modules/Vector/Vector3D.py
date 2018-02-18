#/usr/bin/python3
from math import sqrt
import math

class vector3D:

    def __init__(self, x : float = 0, y : float = 0, z : float = 0):
        self.x = x
        self.y = y
        self.z = z
    def distance_to(self, vector : vector3D) -> float:
        return sqrt((self.x - vector.x) ** 2 + (self.y - vector.y) ** 2 + (self.z - vector.z) ** 2)

    def length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, vector : vector3D):
        return vector3D(self.x + vector.x, self.y + vector.y, self.z + vector.z)
    def scalar_mul(self,vector):
        return self.length() * vector.length() * math.cos(self.angle(vector))
    def angle(self,vector):
        return math.acos((self.x * vector.x + self.y * vector.y + self.z * vector.z) / (self.length() * vector.length()))


