from satprot import *
c =  Connection("192.168.2.109", 14944)
m = OutMsg(1, 1)
m.add_float(60)
m.add_float(60)
m.add_float(60)
c.send(m)