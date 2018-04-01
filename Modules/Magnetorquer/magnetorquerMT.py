from . import magnetorquer
import threading

class magnetorquerMT(magnetorquer.magnetorquer):
    '''
    This class is exactly like magnetorquer, except it allows one to use the class by multiple threads at the same time
    '''

    def __init__(self):
        magnetorquer.magnetorquer.__init__(self)
        self.lock = threading.Lock()

    # Setters
    def set_x(self,x):
        """
        This function sets the field value of the x axis magnetorquer
        
        parameters :
        x -- an int representing the direction of the field, 1 - positive, 0 - none, -1 - negative

        """

        with self.lock:
            self.__set_x__(x)

    def set_y(self,y):
        """
        This function sets the field value of the y axis magnetorquer
        
        parameters :
        y -- an int representing the direction of the field, 1 - positive, 0 - none, -1 - negative

        """

        with self.lock:
            self.__set_y__(y)

    def set_z(self,z):
        """
        This function sets the field value of the z axis magnetorquer
        
        parameters :
        z -- an int representing the direction of the field, 1 - positive, 0 - none, -1 - negative

        """

        with self.lock:
            self.__set_z__(z)

    # Getters
    def get_x(self):
        """ Returns the current x field direction """

        return_x = None
        with self.lock:
            return_x = self.__get_x__()
        return return_x
        
    def get_y(self):
        """ Returns the current y field direction """

        return_y = None
        with self.lock:
            return_y = self.__get_y__()
        return return_y

    def get_z(self):
        """ Returns the current z field direction """

        return_z = None
        with self.lock:
            return_z = self.__get_z__()
        return return_z
