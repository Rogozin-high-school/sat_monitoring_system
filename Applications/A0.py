from ..Modules.Communications import communications
from ..Modules.Magnetometer import magnetometer_factory

import numpy
import time
import math

sensor = magnetometer_factory.initialize()

conn = satprot.Connection('192.168.2.109', 14944)
past = []

while True:
    # While the program runs it
    # Reads values from the magnetometer
    value = sensor.readMagnet()

    # Calculates angle on the xy plane
    angle = math.degrees(numpy.arctan2(value['x'], value['y']))
    
    # Rounds it up a bit
    past.append(angle)
    if len(past) > 5:
        del past[0]

    # Send the angle to the simulation
    msg = satprot.OutMsg(0, 0)
    msg.add_float(0)
    msg.add_float(angle)
    msg.add_float(0)

    conn.send(msg)

    print(angle)

    # Wait for a bit 
    # because the magnetometer refresh rate is 8Hz
    time.sleep(0.125)
