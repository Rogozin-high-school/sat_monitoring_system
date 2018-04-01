from . import HBridge
from .. import config

import threading


class magnetorquer:
    """ This class represents the magnetorquer on the satellite """

    def __init__(self):
        """ Initialing an h-bridge for each axis"""

        self.HBridges = dict()

        HBridges['x'] = HBridge.HBridge(config.X_AXIS_H_BRIDGE_DIRECTION_PORT_1,
                config.X_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                config.X_AXIS_H_BRIDGE_PWM_PORT_1,
                config.X_AXIS_H_BRIDGE_PWM_PORT_2)

        HBridges['y'] = HBridge.HBridge(config.Y_AXIS_H_BRIDGE_DIRECTION_PORT_1,
                config.Y_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                config.Y_AXIS_H_BRIDGE_PWM_PORT_1,
                config.Y_AXIS_H_BRIDGE_PWM_PORT_2)
        
        HBridges['z'] = HBridge.HBridge(config.Z_AXIS_H_BRIDGE_DIRECTION_PORT_1,
                config.Z_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                config.Z_AXIS_H_BRIDGE_PWM_PORT_1,
                config.Z_AXIS_H_BRIDGE_PWM_PORT_2)
    
        self.direction = {'x' : 0, 'y' : 0, 'z' : 0}

        self.lock = threading.Lock()
   
    def __set_x__(self,x):
        """
        This function sets the field value of the x axis magnetorquer
        
        parameters :
        x -- an int representing the direction of the field, 1 - positive, 0 - none, -1 - negative

        """

        # Input vaidation
        try:
            x = int(x)
        except:
            raise ValueError('H Bridge direction is not valid')

        if(x != 0 and x != 1 and x != -1):
            raise ValueError('H Bridge direction is not valid')
        
        self.direction['x'] = x
        self.HBridges['x'].SetDirection(x)
        
    def __set_y__(self,y):
        """
        This function sets the field value of the y axis magnetorquer
        
        parameters :
        y -- an int representing the direction of the field, 1 - positive, 0 - none, -1 - negative

        """

        # Input vaidation
        try:
            y = int(y)
        except:
            raise ValueError('H Bridge direction is not valid')
        
        if(y != 0 and y != 1 and y != -1):
            raise ValueError('H Bridge direction is not valid')
        
        self.direction['y'] = y
        self.HBridges['y'].SetDirection(y)

    def __set_z__(self,z):
        """
        This function sets the field value of the z axis magnetorquer
        
        parameters :
        z -- an int representing the direction of the field, 1 - positive, 0 - none, -1 - negative

        """

        # Input vaidation
        try:
            z = int(z)
        except:
            raise ValueError('H Bridge direction is not valid')
        
        if(z != 0 and z != 1 and z != -1):
            raise ValueError('H Bridge direction is not valid')
        
        self.direction['z'] = z
        self.HBridges['z'].SetDirection(z)

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
