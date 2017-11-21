# ------------ import statements
import socket
import hmc5883l
import time
import threading



# ------------ variables
HOST, PORT = '', 8080
magnetometer = hmc5883l.hmc5883l()
LOG_DELAY_MS = 1000
lock = threading.Lock()
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

# Returns the current x magnetometer reading
def get_x():
    return 'X'

# Returns the current y magnetometer reading
def get_y():
    return 'Y'

# Returns the current z magnetometer reading
def get_z():
    return 'Z'


# ------------ thread
# this other thread will create a log file
class log_thread(threading.Thread):
    def __init(self):
        threading.Thread.__init__(self)

    def run(self):
        while should_log:
            try:
                lock.acquire()
                value_x = get_x()
                value_y = get_y()
                value_z = get_z()
                write_to_log('X:' + get_x() + ' Y:' + get_y() + ' Z:' + get_z())
                lock.release()
                time.sleep(LOG_DELAY_MS/1000.0)
            except KeyboardInterrupt:
                break


# ------------ main code
# Start the logging thread
thread = log_thread()
thread.start()

# Start the http server
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

while True:
    try :
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        
        request_split = request.split(' ')
        if len(request_split) > 1:
            path = request_split[1][1:]
            http_response = "HTTP/1.1 200 OK" + "\n\n"
            if path == "log":
                # writes the log to the http_response
                lock.acquire()
                for line in read_from_log():
                    http_response += line
                lock.release()
            elif path == "measure":
                # writes the current measurments to the http_response
                lock.acquire()
                http_response += "X : " + get_x() + "\n"
                http_response += "Y : " + get_y() + "\n"
                http_response += "Z : " + get_z() + "\n"
                lock.release()
            else :
                http_response += "Command unknown\n"
                http_response += "Available commands are 'log' and 'measure'"

            client_connection.sendall(http_response)
            client_connection.close()
    except KeyboardInterrupt:
        break

should_log = False
print "Ending server"
