from ..Modules.Magnetometer import magnetometer_factory
import math
import time
import math
import numpy

sensor = magnetometer_factory.initialize()

shouldRun = True

while shouldRun:
    try :
        axes = sensor.readMagnet()

        squared_sum = 0.0

        for x in axes:
            axes[x] = round(axes[x], 2)
            squared_sum += axes[x] ** 2
        

        axes_values = str(axes)
        length_value = str(math.sqrt(squared_sum))
        arc_tan_2_value = str(math.degrees(numpy.arctan2(axes['x'], axes['y'])))

        print(", ".join([axes_values, length_value, arc_tan_2_value]))
        
        time.sleep(0.125)
    except KeyboardInterrupt:
        shouldRun = False
