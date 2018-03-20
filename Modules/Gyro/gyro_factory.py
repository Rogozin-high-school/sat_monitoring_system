from . import config
from . import fake_mpu
if config.GYRO_CONNECTED:
    from . import mpu9250
#this function returns the mpu9250 hardware module object if the hardware is connected.
#otherwise returns and object that simulates hardware 
def initialize():
    if(config.GYRO_CONNECTED == True):
        return mpu9250.mpu9250()
    else:
        return fake_mpu.fake_mpu()