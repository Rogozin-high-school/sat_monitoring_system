from ..Modules.Accelerometer import accelerometerMT

sensor = accelerometerMT.accelerometerMT()

shouldRun = True

while shouldRun:
    try :
        axes = sensor.get_axes()
        x = axes[0]
        y = axes[1]
        z = axes[2]

        print ("x:%8.3f    y:%8.3f    z:%8.3f" % (x, y, z))
    except KeyboardInterrupt:
        shouldRun = False
