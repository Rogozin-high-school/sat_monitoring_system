from ..Communication import satprot
from ..Modules.Control import Control
import time
con = satprot.connection("192.168.2.104",14944)
while(True):
    time.sleep(0.05)
    t = time.time()
    direction = (Control.get_angle(t))
    msg = satprot.OutMsg(1,0)
    msg.add_float(direction[0])
	msg.add_float(direction[1])
	msg.add_float(direction[2])
    print("x:" + direction[0] + " y:" + direction[1] + " z:" + direction[2])
    con.send(msg)