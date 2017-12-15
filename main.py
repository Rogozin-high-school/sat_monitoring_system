# ------------ Import statements
import threading
import socket

# ------------ Local import statements
import magnetometer
import log_thread
import config
import log

# ------------ Variables & Objects
log_lock = threading.Lock()
magnetometer_lock = threading.Lock()
magnetometer = magnetometer.magnetometer()
log = log.log()
log_thread = log_thread.log_thread(magnetometer_lock, log_lock, magnetometer, log)

# ------------ main code
# Starting logger thread
log_thread.start()

# Start the http server
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((config.HTTP_HOST, config.HTTP_PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % config.HTTP_PORT

while True:
    try :
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        
        request_split = request.split(' ')
        if len(request_split) > 1:
            path = request_split[1][1:]
            print path
        
            # http header
            http_response = "HTTP/1.1 200 OK\n"
            http_response += "Content-Type: text/html\n"
            http_response += "Connection: close\n"
            http_response += "\n"
            
            if path == "log":
                # writes the log to the http_response
                with log_lock:
                    for line in log.read_from_log():
                        http_response += line + "</br>"
            elif path == "measure":
                # writes the current measurments to the http_response
                with magnetometer_lock :
                    http_response += "'X':" + str(magnetometer.get_x()) + ","
                    http_response += "'Y':" + str(magnetometer.get_y()) + ","
                    http_response += "'Z':" + str(magnetometer.get_z())
            elif path == "live":
                data_file = open(config.LIVE_DISPLAY_FILE_NAME, 'r')
                http_response += ''.join(data_file.readlines())
            else :
                http_response += "Command unknown</br>"
                http_response += "Available commands are 'log' and 'measure'"

            client_connection.sendall(http_response)
            client_connection.close()
    except KeyboardInterrupt:
        break

# Stopping logger thread
log_thread.stop()
