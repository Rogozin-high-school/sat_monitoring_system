from . import hBridge
from .. import config

import threading


class magnetorquer:
    def __init__(self):
        self.x = hBridge.hBridge(X_AXIS_H_BRIDGE_DIRECTION_PORT_1
                X_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                X_AXIS_H_BRIDGE_PWM_PORT_1,
                X_AXIS_H_BRIDGE_PWM_PORT_2)

        self.y = hBridge.hBridge(Y_AXIS_H_BRIDGE_DIRECTION_PORT_1
                Y_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                Y_AXIS_H_BRIDGE_PWM_PORT_1,
                Y_AXIS_H_BRIDGE_PWM_PORT_2)
        
        self.z = hBridge.hBridge(Z_AXIS_H_BRIDGE_DIRECTION_PORT_1
                Z_AXIS_H_BRIDGE_DIRECTION_PORT_2,
                Z_AXIS_H_BRIDGE_PWM_PORT_1,
                Z_AXIS_H_BRIDGE_PWM_PORT_2)
    
        self.xDirection = 0
        self.yDirection = 0
        self.zDirection = 0

        self.lock = threading.Lock()
   
        
    # Setters
    def __set_x__(self,x):
        # Input vaidation
        if(x != 0 && x != 1 && x != -1):
            raise ValueError('H Bridge direction is not valid')
        
        self.xDirection = x
        self.x.SetDirection(x)
        

    def __set_y__(self,y):
        # Input vaidation
        if(y != 0 && y != 1 && y != -1):
            raise ValueError('H Bridge direction is not valid')
        
        self.yDirection = y
        self.y.SetDirection(y)

    def __set_z__(self,z):
        # Input vaidation
        if(z != 0 && z != 1 && z != -1):
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
