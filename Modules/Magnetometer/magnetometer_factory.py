from . import config

# Has an initialize method that returns an object representing a magnetometer
# Whether one is connected or not

if config.MAGNETOMETER_CONNECTED:
    # If the magnetometer is connected

    from . import mpu9250
    
    def __init_hardware():
        return mpu9250.MPU9250()

    initialize = __init_hardware
else:
    # If the magnetometer is not connected

    from . import fake_magnetometer

    def __init_fake_hardware():
        return fake_magnetometer.fake_magnetometer()
    
    initialize = __init_fake_hardware
