from . import hBridge
from .. import config

import threading


class magnetorquer:
    '''
    This class is used to create certain field on the magnetorquers on the satellite for each axis.
    There are 3 axis (x,y,z) and each one could be changed.
    The init function  initiates the connections of the object to the 3 physical magnetorqures.
    '''
    def __init__(self):
        """ Initialing an h-bridge for each axis"""

        self.hBridges = dict()

        hBridges['x'] = hBridge.hBridge(config.X_AXIS_H_BRIDGE_DIRECTION_PORT_1,
                config.X_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                config.X_AXIS_H_BRIDGE_PWM_PORT_1,
                config.X_AXIS_H_BRIDGE_PWM_PORT_2)

        hBridges['y'] = hBridge.hBridge(config.Y_AXIS_H_BRIDGE_DIRECTION_PORT_1,
                config.Y_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                config.Y_AXIS_H_BRIDGE_PWM_PORT_1,
                config.Y_AXIS_H_BRIDGE_PWM_PORT_2)
        
        hBridges['z'] = hBridge.hBridge(config.Z_AXIS_H_BRIDGE_DIRECTION_PORT_1,
                config.Z_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                config.Z_AXIS_H_BRIDGE_PWM_PORT_1,
                config.Z_AXIS_H_BRIDGE_PWM_PORT_2)
    
        self.direction = {'x' : 0, 'y' : 0, 'z' : 0}

        self.lock = threading.Lock()
   
    def __set_x__(self,x):
        """This function sets the field value of the x axis magnetorquer"""

        # Input vaidation
        try:
            x = int(x)
        except:
            raise ValueError('H Bridge direction is not valid')

        if(x != 0 and x != 1 and x != -1):
            raise ValueError('H Bridge direction is not valid')
        
        self.direction['x'] = x
        self.hBridges['x'].SetDirection(x)
        
    def __set_y__(self,y):
        """This function sets the field value of the y axis magnetorquer"""

        # Input vaidation
        try:
            y = int(y)
        except:
            raise ValueError('H Bridge direction is not valid')
        
        if(y != 0 and y != 1 and y != -1):
            raise ValueError('H Bridge direction is not valid')
        
        self.direction['y'] = y
        self.hBridges['y'].SetDirection(y)

    def __set_z__(self,z):
        """This function sets the field value of the z axis magnetorquer"""

        # Input vaidation
        try:
            z = int(z)
        except:
            raise ValueError('H Bridge direction is not valid')
        
        if(z != 0 and z != 1 and z != -1):
            raise ValueError('H Bridge direction is not valid')
        
        self.direction['z'] = z
        self.hBridges['z'].SetDirection(z)

    # Getters
    def __get_x__(self):
        """ Returns the current x axis magnetorquer value """
        return self.Direction['x']

    def __get_y__(self):
        """ Returns the current y axis magnetorquer value """
        return self.Direction['y']

    def __get_z__(self):
        """ Returns the current z axis magnetorquer value """
        return self.Direction['z']
