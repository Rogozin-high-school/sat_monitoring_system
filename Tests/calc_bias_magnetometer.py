from ..Modules.Magnetometer import magnetometer_factory

sensor = magnetometer_factory.initialize()

# A 2D array of size 3 by 2, that would store the max and min values for each axis
bias = [[None, None], [None, None], [None, None]]
axis_names = ['x', 'y', 'z']

try:
    while True:
        field = sensor.readMagnet()
        for axis in bias:
            if axis[0] == None or field[axis] < axis[0]:
                axis[0] = field[axis]
            elif axis[1] == None or field[axis] > axis[1]:
                axis[1] = field[axis]
except KeyboardInterrupt:
    for axis in bias:
        bias = (axis[0] + axis[1]) / 2
        print(axis_names[axis] + " : " + bias)
