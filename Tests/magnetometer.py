from ..Modules.Magnetometer import magnetometerMT
import math
import time

sensor = magnetometerMT.magnetometerMT()

shouldRun = True

while shouldRun:
    try :
        axes = sensor.get_axes()
        
        print(axes)
        
        time.sleep(0.125)
    except KeyboardInterrupt:
        shouldRun = False
