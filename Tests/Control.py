from ..Modules.Control import Control
import json

angles = [90,45,0,180,360,30,60,40]
 
for i in angles:
    print(str(i)+"->"+str(Control.get_angle_vector(i)))

noting = input("Press Enter to Continue...")