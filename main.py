# ------------ Import statements
import socket

# ------------ Local import statements
import magnetometerMT
import log_thread
import config
import log

# ------------ Variables & Objects
log = log.log(config.LOG_FILE_NAME)
magnetometer = magnetometerMT.magnetometerMT()
log_thread = log_thread.log_thread(magnetometer, log)

# ------------ main code
# Starting logger thread
log_thread.start()

# Start the http server
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((config.HTTP_HOST, config.HTTP_PORT))
listen_socket.listen(1)

while True:
    try :
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        
        request_split = str(request).split(' ')
        if len(request_split) > 1:
            # Processing the request and splitting to path and parameters
            path_and_parameters = request_split[1][1:].split('?')
            path = path_and_parameters[0]
            parameters = []
            parameters_dict = dict()

            # Creating a dictionary that contains the parameters data
            if len(path_and_parameters) == 2:
                parameters = path_and_parameters[1].split('&')
                for x in parameters:
                    split_paramter = x.split("=")
                    if len(split_paramter) == 2:
                        parameters_dict[split_paramter[0]] = split_paramter[1]

            print("There was a request to " + path)

            # http header
            http_response = "HTTP/1.1 200 OK\n"
            http_response += "Content-Type: text/html\n"
            http_response += "Connection: close\n"
            http_response += "\n"
            
            if path == "log":
                # writes the log to the http_response
                for line in log.read_from_log():
                    http_response += line + "</br>"
            elif path == "measure":
                # writes the current measurments to the http_response
                http_response += "'X':" + str(magnetometer.get_x()) + ","
                http_response += "'Y':" + str(magnetometer.get_y()) + ","
                http_response += "'Z':" + str(magnetometer.get_z())
            elif path == "live":
                data_file = open(config.LIVE_DISPLAY_FILE_NAME, 'r')
                http_response += ''.join(data_file.readlines())
            elif "set" in path:
                parameters_dict = dict()
                parameters_list = path.split("&")
            else :
                http_response += "Command unknown</br>"
                http_response += "Available commands are 'log' and 'measure'"

            client_connection.sendall(http_response.encode())
            client_connection.close()
    except KeyboardInterrupt:
        break

# Stopping logger thread
log_thread.stop()
