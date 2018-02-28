from ..Modules.Control import Control
import json

angles = [90,45,0,180,360,30,60]
 
for i in angles:
    print(str(i)+"->")
    print(Control.get_angle_vector(i))

noting = raw_input("Enter any key to continue...")