from ..Modules.Magnetometer import magnetometer_factory
import math
import time

sensor = magnetometer_factory.initialize()

shouldRun = True

while shouldRun:
    try :
        axes = sensor.readMagnet()
        
        print(axes)
        
        time.sleep(0.125)
    except KeyboardInterrupt:
        shouldRun = False
