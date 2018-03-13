from ..Modules.Gyro import gyroMT
from ..Communication import satprot
import time

sensor = gyroMT.gyroMT()

shouldRun = True

con = satprot.connection("192.168.2.104")

while shouldRun:
    try :
        axes = sensor.get_axes()
        x = axes[0]
        y = axes[1]
        z = axes[2]
        msg = satprot.OutMsg(1,0)
        msg.add_float(x)
        msg.add_float(y)
        msg.add_float(z)
        print ("x:%8.3f    y:%8.3f    z:%8.3f" % (x, y, z))
        con.send(msg)
    except KeyboardInterrupt:
        shouldRun = False
