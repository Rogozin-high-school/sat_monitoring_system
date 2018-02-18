from . import hBridge
from .. import config

import threading


class magnetorquer:
    def __init__(self):
        self.x = hBridge.hBridge(config.X_AXIS_H_BRIDGE_DIRECTION_PORT_1,
                config.X_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                config.X_AXIS_H_BRIDGE_PWM_PORT_1,
                config.X_AXIS_H_BRIDGE_PWM_PORT_2)

        self.y = hBridge.hBridge(config.Y_AXIS_H_BRIDGE_DIRECTION_PORT_1,
                config.Y_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                config.Y_AXIS_H_BRIDGE_PWM_PORT_1,
                config.Y_AXIS_H_BRIDGE_PWM_PORT_2)
        
        self.z = hBridge.hBridge(config.Z_AXIS_H_BRIDGE_DIRECTION_PORT_1,
                config.Z_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                config.Z_AXIS_H_BRIDGE_PWM_PORT_1,
                config.Z_AXIS_H_BRIDGE_PWM_PORT_2)
    
        self.xDirection = 0
        self.yDirection = 0
        self.zDirection = 0

        self.lock = threading.Lock()
   
        
    # Setters
    def __set_x__(self,x):
        # Input vaidation

        # What if we got the string '1' ?
        try:
            x = int(x)
        except:
            raise ValueError('H Bridge direction is not valid')

        if(x != 0 and x != 1 and x != -1):
            raise ValueError('H Bridge direction is not valid')
        
        self.xDirection = x
        self.x.SetDirection(x)
        

    def __set_y__(self,y):
        # Input vaidation

        # What if we got the string '1' ?
        try:
            y = int(y)
        except:
            raise ValueError('H Bridge direction is not valid')
        
        if(y != 0 and y != 1 and y != -1):
            raise ValueError('H Bridge direction is not valid')
        
        self.yDirection = y
        self.y.SetDirection(y)

    def __set_z__(self,z):
        # Input vaidation

        # What if we got the string '1' ?
        try:
            z = int(z)
        except:
            raise ValueError('H Bridge direction is not valid')
        
        if(z != 0 and z != 1 and z != -1):
            raise ValueError('H Bridge direction is not valid')
        
        self.zDirection = z
        self.z.SetDirection(z)

    # getters
    def __get_x__(self):
        return self.xDirection

    def __get_y__(self):
        return self.yDirection

    def __get_z__(self):
        return self.zDirection
