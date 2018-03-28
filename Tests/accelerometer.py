from ..Modules.Accelerometer import accelerometerMT
import time

sensor = accelerometerMT.accelerometerMT()

shouldRun = True

try:
    while shouldRun:
        time.sleep(0.05)
        axes = sensor.get_axes()
        x = axes[0]
        y = axes[1]
        z = axes[2]
        print ("x:%8.3f    y:%8.3f    z:%8.3f" % (x, y, z))
except KeyboardInterrupt:
    shouldRun = False
