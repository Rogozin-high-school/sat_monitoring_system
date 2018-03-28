from ..Modules.Magnetometer import magnetometer_factory
import math
import time
import math

sensor = magnetometer_factory.initialize()

shouldRun = True

while shouldRun:
    try :
        axes = sensor.readMagnet()

        squared_sum = 0.0

        for x in axes:
            axes[x] = round(axes[x], 2)
            squared_sum += axes[x] ** 2
        

        print(str(axes) + ", length : " + str(math.sqrt(squared_sum)))
        
        
        time.sleep(0.125)
    except KeyboardInterrupt:
        shouldRun = False
