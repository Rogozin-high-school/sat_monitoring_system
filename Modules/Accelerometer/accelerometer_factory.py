from . import config

if config.ACCELEROMETER_CONNECTED:
    from . import mpu9250

    def __init_hardware():
        return mpu9250.mpu9250()

    initialize = __init_hardware

else:
    from . import fake_accelerometer

    def __init_fake_hardware():
        return fake_accelerometer.fake_accelerometer()

    initialize = __init_fake_hardware
