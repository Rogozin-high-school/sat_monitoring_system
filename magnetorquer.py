import threading

class magnetorquer:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0
		#ports for real life magnetorquer
		self.port_x = 0
		self.port_y = 0
		self.port_z = 0
		self.lock = threading.Lock()
	
	# Update the magnetorquer according the saved x,y,z values
	def __update(self):
		self.implemented = False

	# Setters
	def __set_x(self,x):
		self.x = x
		
	def __set_y(self,y):
		self.y = y
	
	def __set_z(self,z):
		self.z = z

	def __set_axes(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	
	# getters
	def __get_x(self):
		return self.x

	def __get_y(self):
		return self.y

	def __get_z(self):
		return self.z

	def __get_axes(self):
		return self.x, self.y, self.z