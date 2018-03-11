from ..Communication import satprot
from ..Modules.Control import Control
import time
con = satprot.connection("127.0.0.1",14944)
while(True):
    time.sleep(0.05)
    t = time.time()
    direction = Control.get_angle_vector(Control.get_angle(t))
    msg = satprot.OutMsg("t",0)
    msg.add_float(direction[0],direction[1],direction[2])
    print("x:" + direction[0] + " y:" + direction[1] + " z:" + direction[2])
    con.send(msg)