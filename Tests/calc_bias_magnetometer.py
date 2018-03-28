from ..Modules.Magnetometer import magnetometer_factory

sensor = magnetometer_factory.initialize()

# A 2D array of size 3 by 2, that would store the max and min values for each axis
bias = [[None, None], [None, None], [None, None]]
axis_names = ['x', 'y', 'z']
initialized = False


try:
    while True:
        field = sensor.readMagnet()

        if not initialized:
            bias[0][0] = field['x']
            bias[0][1] = field['x']

            bias[1][0] = field['y']
            bias[1][1] = field['y']

            bias[2][0] = field['z']
            bias[2][1] = field['z']

        else:
            for axis in range(len(axis)):
                bias[axis][0] = min(field[axis_names[axis]], bias[axis][0])
                bias[axis][1] = max(field[axis_names[axis]], bias[axis][0])

except KeyboardInterrupt:
    for axis in bias:
        bias = (axis[0] + axis[1]) / 2
        print(axis_names[axis] + " : " + bias)
