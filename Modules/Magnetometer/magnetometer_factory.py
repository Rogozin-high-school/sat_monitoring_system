from . import config

if config.MAGNETOMETER_CONNECTED:
    from . import mpu9250
else:
    from . import fake_magnetometer



#this function returns the mpu9250 hardware module object if the hardware is connected.
#otherwise returns and object that simulates hardware
def initialize():
    if(config.MAGNETOMETER_CONNECTED == True):
        return mpu9250.MPU9250()
    else:
        return fake_magnetometer.fake_magnetometer()
