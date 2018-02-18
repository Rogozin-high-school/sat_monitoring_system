#/usr/bin/python3
from math import sqrt
import math

class vector2D:

    def __init__(self, x : float = 0, y : float = 0):
        self.x = x
        self.y = y
    def distance_to(self, vector : vector2D) -> float:
        return sqrt((self.x - vector.x) ** 2 + (self.y - vector.y) ** 2)

    def length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, vector : vector2D):
        return vector2D(self.x + vector.x, self.y + vector.y)
		
	def __mul__(self,vector):
		vector2 = vector2D()
        return vector2
		
	def scalar_mul(self,vector):
		return self.length() * vector.length() * math.cos(self.angle(vector))
	def angle(self,vector):
		return math.acos((self.x * vector.x + self.y * vector.y) / (self.length() * vector.length()))

