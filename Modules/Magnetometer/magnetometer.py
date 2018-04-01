from . import magnetometer_factory


class magnetometer:
    """A class for reading data from the magnetometer sensor"""

    def __init__(self):
        """
        Initialises the sensor object if the
        magnetometer is connected
        """

        self.sensor = magnetometer_factory.initialize()

    def __get_axes__(self):
        """
        Reads magnetic field in a form of a tuple containing
        x, y and z axis values
        """

        return self.sensor.readMagnet()
