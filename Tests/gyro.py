from ..Modules.Gyro import gyroMT
from ..Communication import satprot
import time

sensor = gyroMT.gyroMT()

shouldRun = True

__DESTINATION__ = "192.168.2.104",14944
con = satprot.connection(__DESTINATION__)

while shouldRun:
    time.sleep(0.05)
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
