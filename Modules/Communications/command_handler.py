from .. import config

class command_handler:
    def __init__(self, magnetometer, magnetorquer, log, gyro, accelerometer):
        self.magnetometer = magnetometer
        self.magnetorquer = magnetorquer
        self.log = log
        self.gyro = gyro
        self.acceleromter = accelerometer
        

    def get_log(self, parameters):
        http_reponse = ""

        for line in self.log.read_from_log():
            http_response += line + "</br>"
        
        return http_response

    def get_magnetorquer(self, parameters):
        output = "'X':" + str(self.magnetorquer.get_x()) + ","
        output += "'Y':" + str(self.magnetorquer.get_y()) + ","
        output += "'Z':" + str(self.magnetorquer.get_z())
        return output
    

    def set_magnetorquer(self, parameters):
        # Updates the values stored by the magnetorquer objects
        if 'x' in parameters:
            self.magnetorquer.set_x(parameters['x'])
        if 'y' in parameters:
            self.magnetorquer.set_y(parameters['y'])
        if 'z' in parameters:
            self.magnetorquer.set_z(parameters['z'])
        return "ok"

    def live(self, parameters):
        # TODO : Make this multithreading safe
        data_file = open(config.LIVE_DISPLAY_FILE_NAME, 'r')
        http_response = ''.join(data_file.readlines())
        return http_response

    def get_magnetometer(self, paramters):
        output = "'X':" + str(self.magnetometer.get_x()) + ","
        output += "'Y':" + str(self.magnetometer.get_y()) + ","
        output += "'Z':" + str(self.magnetometer.get_z())
        return output
