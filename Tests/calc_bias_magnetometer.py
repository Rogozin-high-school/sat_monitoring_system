from ..Modules.Magnetometer import magnetometer_factory
import time

sensor = magnetometer_factory.initialize()

# A 2D array of size 3 by 2, that would store the max and min values for each axis
bias = [[None, None], [None, None], [None, None]]
axis_names = ('x', 'y', 'z')

# Like min but if one of the values is None then it returns the other one
def betterMin(value1, value2):
    if value1 == None and value2 != None:
        return value2
    elif value2 == None and value1 != None:
        return value1
    else:
        return min(value1, value2)
    
# Like max but if one of the values is None then it returns the other one
def betterMax(value1, value2):
    if value1 == None and value2 != None:
        return value2
    elif value2 == None and value1 != None:
        return value1
    else:
        return max(value1, value2)


try:
    print("Reading magnetometer data")

    while True:
        field = sensor.readMagnet()

        for i in range(3):
            bias[i][0] = betterMin(bias[i][0], field[axis_names[i]])
            bias[i][1] = betterMax(bias[i][1], field[axis_names[i]])

        time.sleep(0.125)

except KeyboardInterrupt:
    print(bias)
    print("------------------")

    print("x:" + str((bias[0][0] + bias[0][1]) / 2))
    print("y:" + str((bias[1][0] + bias[1][1]) / 2))
    print("z:" + str((bias[2][0] + bias[2][1]) / 2))
