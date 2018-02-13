from . import magnetometerMT

sensor = magnetometerMT.magnetometerMT()

while True:
    try:
        print sensor.get_axes()
    except KeyboardInterrupt:
        break
