from . import gyro_factory

class gyro:
    """A class for reading data from the gyro sensor"""

    def __init__(self):
        """Initialises the sensor object if the
        gyro is connected"""

        self.sensor = gyro_factory.initialize()

    def __get_axes__(self):
        """Reads gyro in a form of a tuple containing
        x, y and z axis values"""

        return self.sensor.gyro
			
