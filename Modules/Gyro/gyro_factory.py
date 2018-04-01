from . import config

# Has an initialize method that returns an object representing a gyro
# Whether one is connected or not

if config.GYRO_CONNECTED:
    # If the gyro is connected

    from . import mpu9250

    def __init_hardware():
        return mpu9250.mpu9250()

    initialize = __init_hardware

else:
    # If the gyro is not connected

    from . import fake_gyro

    def __init_fake_hardware():
        return fake_gyro.fake_gyro()

    initialize = __init_fake_hardware
