from . import accelerometer_factory

class accelerometer:
    """A class for reading data from the accelerometer sensor"""

    def __init__(self):
        """Initialises the sensor object if the
        accelerometer is connected"""
        self.sensor = accelerometer_factory.initialize()

    def __get_axes__(self):
        """
        Measure acceleration in a form of a tuple containing
        x, y and z axis values
        """
        
        return self.sensor.accel
