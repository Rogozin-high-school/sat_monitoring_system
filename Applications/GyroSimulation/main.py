import serial
from satprot import *
import numpy as np

c = Connection("localhost", 14944)

vec = np.zeros(3)

ard = serial.Serial("COM8", 9600, timeout=5)

while (True):
    try:
        a = str(ard.readline(), "utf-8")
        b = np.array([float(x) if abs(float(x)) > 1 else 0 for x in a.split(",")]) * 0.02
        b[0], b[1] = b[1], b[0]
        vec += b
        print(vec)
        m = OutMsg(1, 1)
        m.add_float(vec[0])
        m.add_float(vec[1])
        m.add_float(vec[2])
        c.send(m)
        print("Sent")
    except:
        pass