import threading

class torquer:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0
		self.lock = threading.Lock()
	def setX(self,xVal):
		with self.lock:
			self.x = xVal #TODO : change to actual set of values
	def setY(self,yVal):
		with self.lock:
			self.y = yVal #TODO : change to actual set of values
	def setZ(self,zVal):
		with self.lock:
			self.z = zVal #TODO : change to actual set of values
	def getValue(self):
		data = None
		with self.lock:
			data  = self.x,self.y,self.z
		return data
