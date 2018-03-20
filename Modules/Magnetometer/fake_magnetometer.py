from . import config

class fake_magnetometer:

    #TODO : add real field simulation
    def readMagnet(self):
        return (0, 0, 0)

