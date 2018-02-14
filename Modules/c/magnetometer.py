from ..Magnetometer import magnetometerMT

sensor = magnetometerMT.magnetometerMT()

shouldRun = True

while shouldRun:
    try :
        axes = sensor.get_axes()
        print ("%8.3f,%8.3f,%8.3f" % (axes[0], axes[1], axes[2]))
    except KeyboardInterrupt:
        shouldRun = False
