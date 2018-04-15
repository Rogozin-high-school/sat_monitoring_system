from . import config

'''
Has initialize method that returns the MT 3d magnetorquer.
When the MT is disconnected, it will return a fake object just
for the code to work
'''

axis_connections = [config.X_AXIS_H_BRIDGE_CONNECTED
,config.Y_AXIS_H_BRIDGE_CONNECTED
,config.Z_AXIS_H_BRIDGE_CONNECTED]

if False in axis_connections:
    # The block for a connected magnetorquer, creates a real object
    from . import magnetorquerMT
    
    def __init_hardware():
        return magnetorquerMT.magnetorquerMT()
    
    initialize = __init_hardware
else:
    # The block for a not connected magnetoruqer, creates a fake object
    from . import fake_magnetorquer

    def __fake():
        return fake_magnetorquer.fake_magnetorquer()
    
    initialize = __fake
    

