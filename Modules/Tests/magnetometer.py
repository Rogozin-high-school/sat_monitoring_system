from ..Magnetometer import magnetometerMT
import math


sensor = magnetometerMT.magnetometerMT()

shouldRun = True

while shouldRun:
    try :
        axes = sensor.get_axes()
        x = axes[0]
        y = axes[1]
        z = axes[2]
        length = math.sqrt(x*x + y*y + z*z)

        print ("x:%8.3f    y:%8.3f    z:%8.3f    length:" % (x, y, z, length))
    except KeyboardInterrupt:
        shouldRun = False
