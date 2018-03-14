from ..Modules.Satprot import satprot
from ..Modules.Control import Control
import time
con = satprot.Connection(input("Enter target ip: "),14944)
while(True):
    time.sleep(0.05)
    t = time.time()
    direction = (Control.get_angle(t))
    msg = satprot.OutMsg(1,0)
    msg.add_float(direction)
    msg.add_float(0)
    msg.add_float(0)
    print("angle: "+str(direction))
    con.send(msg)