import threading

class magnetorquer:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.lock = threading.Lock()
    
    # Update the magnetorquer according the saved x,y,z values
    def __update__(self):
        self.implemented = False

    # Setters
    def __set_x__(self,x):
        self.x = x
            
    def __set_y__(self,y):
        self.y = y
    
    def __set_z__(self,z):
        self.z = z

    # getters
    def __get_x__(self):
        return self.x

    def __get_y__(self):
        return self.y

    def __get_z__(self):
        return self.z
