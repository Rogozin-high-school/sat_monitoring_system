from Modules.Satprot import satprot
from Modules.Magnetometer import magnetometer_factory

import numpy
import time
import math

sensor = magnetometer_factory.initialize()

conn = satprot.Connection('192.168.2.109', 14944)
past = []

while True:
    value = sensor.readMagnet()
    angle = math.degrees(numpy.arctan2(value['x'], value['y']))
    
    past.append(angle)
    if len(past) > 5:
        del past[0]

    #//angle = sum(past[i] / (math.sqrt(i)+ 1) for i in range(len(past))) / sum(1 / (math.sqrt(i) + 1) for i in range(len(past)))

    msg = satprot.OutMsg(0,0)
    msg.add_float(0)
    msg.add_float(angle)
    msg.add_float(0)

    conn.send(msg)

    print(angle)

    time.sleep(0.125)
