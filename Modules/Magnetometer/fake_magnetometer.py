class fake_magnetometer:
    """Simulates a magnetometer sensor"""

    #TODO : add real field simulation
    def readMagnet(self):
        return {'x': 0.0, 'y': 0.0, 'z': 0.0}
