from . import config

if config.GYRO_CONNECTED:
    from . import mpu9250

    def __init_hardware():
        return mpu9250.mpu9250()

    initialize = __init_hardware

else:
    from . import fake_gyro

    def __init_fake_hardware():
        return fake_gyro.fake_gyro()

    initialize = __init_fake_hardware
