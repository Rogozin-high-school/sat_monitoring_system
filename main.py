# ------------ import statements
import socket
import time
import threading

# ------------ local import statements
import config
import magnetometer

# ------------ variables
sensor = magnetometer.magnetometer()
log_lock = threading.Lock()
magnetometer_lock = threading.Lock()
should_log = True

# ------------ methods
# TODO : Implement these methods
# Writes data to the log file
def write_to_log(text):
    current_time = time.strftime("%d/%m/%Y-%H:%M:%S")
    f = open('log', 'a+')
    f.write(current_time + '|' + text + '\n')
    f.flush()
    f.close()

def read_from_log():
    f=open('log', 'r+')
    data = f.readlines()
    f.close()
    return data

# ------------ thread
# this other thread will create a log file
class log_thread(threading.Thread):
    def __init(self):
        threading.Thread.__init__(self)

    def run(self):
        while should_log:
            try:
                value_x = None
                value_y = None
                value_z = None
                
                # reading data from the magnetometer
                with magnetometer_lock:
                    value_x = sensor.get_x()
                    value_y = sensor.get_y()
                    value_z = sensor.get_z()
                
                # writing to the log file
                with log_lock:
                    write_to_log('X:' + str(value_x) + ' Y:' + str(value_y) + ' Z:' + str(value_z))
                
                time.sleep(config.LOG_INTERVAL_MS/1000.0)
            except KeyboardInterrupt:
                break


# ------------ main code
# making sure the log file exists
f = open('log', 'w+')
f.close()

# Start the logging thread
thread = log_thread()
thread.start()

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
            # http header
            http_response = "HTTP/1.1 200 OK\n"
            http_response += "Content-Type: text/html\n"
            http_response += "Connection: close\n"
            http_response += "\n"
            
            if path == "log":
                # writes the log to the http_response
                with log_lock:
                    for line in read_from_log():
                        http_response += line + "</br>"
            elif path == "measure":
                # writes the current measurments to the http_response
                with magnetometer_lock :
                    http_response += "'X':" + str(sensor.get_x()) + ","
                    http_response += "'Y':" + str(sensor.get_y()) + ","
                    http_response += "'Z':" + str(sensor.get_z())
            elif path == "live":
                data_file = open('live.html', 'r')
                http_response += ''.join(data_file.readlines())
            else :
                http_response += "Command unknown</br>"
                http_response += "Available commands are 'log' and 'measure'"

            client_connection.sendall(http_response)
            client_connection.close()
    except KeyboardInterrupt:
        break

should_log = False
print "Ending server"