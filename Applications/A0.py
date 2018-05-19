from ..Modules.Communications import communications
from ..Modules.Magnetometer import magnetometer_factory

import numpy
import time
import math

sensor = magnetometer_factory.initialize()

conn = communications.Connection('10.17.110.20', 14944)

t=0
while True:
    
    t=t+1
    ang = t%360
    # Send the angle to the simulation
    msg = communications.OutMsg(0, 0)
    msg.add_float(numpy.cos(numpy.radians(ang))*30)
    msg.add_float(numpy.sin(numpy.radians(ang))*30)

    conn.send(msg)
    #print(numpy.sin(numpy.radians(ang))*30)

    # Wait for a bit 
    # because the magnetometer refresh rate is 8Hz
    time.sleep(0.13)
