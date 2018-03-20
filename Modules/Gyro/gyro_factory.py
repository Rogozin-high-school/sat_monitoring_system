from . import config

if config.GYRO_CONNECTED:
    from . import mpu9250
else:
    from . import fake_gyro

#this function returns the mpu9250 hardware module object if the hardware is connected.
#otherwise returns and object that simulates hardware 
def initialize():
    if(config.GYRO_CONNECTED == True):
        return mpu9250.mpu9250()
    else:
        return fake_gyro.fake_gyro()
