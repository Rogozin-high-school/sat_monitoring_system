from . import config


if config.MAGNETOMETER_CONNECTED:
    from . import mpu9250
    
    def __init_hardware():
        return mpu9250.MPU9250()

    initialize = __init_hardware
else:
    from . import fake_magnetometer

    def __init_fake_hardware():
        return fake_magnetometer.fake_magnetometer()
    
    initialize = __init_fake_hardware
