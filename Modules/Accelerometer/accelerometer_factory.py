from . import config

# Has an initialize method that returns an object representing a accelerometer
# Whether one is connected or not

if config.ACCELEROMETER_CONNECTED:
    # If the accelerometer is connected

    from . import mpu9250

    def __init_hardware():
        return mpu9250.mpu9250()

    initialize = __init_hardware

else:
    # If the accelerometer is not connected

    from . import fake_accelerometer

    def __init_fake_hardware():
        return fake_accelerometer.fake_accelerometer()

    initialize = __init_fake_hardware
