from . import config
from . import fake_mpu
if config.MAGNETOMETER_CONNECTED:
    from . import mpu9250
def initialize():
    if(config.GYRO_CONNECTED == True):
        return mpu9250.mpu9250()
    else:
        return fake_mpu.fake_mpu()