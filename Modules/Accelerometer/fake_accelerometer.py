class fake_accelerometer:
    """Simulates an accelerometer sensor"""

    @property
    def accel(self):
        """ A tuple contating acceleration values in 3 axis """

        return (0, 0, 0)
