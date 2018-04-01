class fake_magnetometer:
    """Simulates a magnetometer sensor"""

    def readMagnet(self):
        """ A dictionary with fake magnetomter values"""
        return {'x': 0.0, 'y': 0.0, 'z': 0.0}
