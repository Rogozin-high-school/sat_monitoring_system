# ------------ import statements
import socket
import hmc5883l
import time
import thread

# ------------ variables
HOST, PORT = '', 8080
magnetometer = hmc5883l.hmc5883l()
f = open('log', 'a+')
LOG_DELAY_MS = 500
    
# ------------ methods
# TODO : Implement this methods
# writes data to the log file
def WriteToLog(text):
    currentTime = time.strftime("%d/%m/%Y:%H:%M:%S")
    f.write(currentTime + '|' + text + '\n')

# returns the current x magnetometer reading
def GetX():
    return 'X'

# returns the current y magnetometer reading
def GetY():
    return 'Y'

# returns the current z magnetometer reading
def GetZ():
    return 'Z'


# ------------ thread
# this other thread will create a log file
def loggingThread(delay):
    while True:
        try:
            ValueX = GetX()
            ValueY = GetY()
            ValueZ = GetZ()
            WriteToLog('X:' + GetX() + ' Y:' + GetY() + ' Z:' + GetZ())
            print("Logged data")
            time.sleep(delay/1000.0)
        except KeyboardInterrupt:
            break


# ------------ main code
# start logging thread
thread.start_new_thread(loggingThread, (LOG_DELAY_MS,))

# start http server
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

while True:
    try :
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        print request

        http_response = "HTTP/1.1 200 OK" + "\n\n"
        http_response += "<h1>Satellite Monitoring System</h1>" + "\n"
        http_response += "X : " + GetX() + "</br>"
        http_response += "Y : " + GetY() + "</br>"
        http_response += "Z : " + GetZ() + "</br>"

        
        client_connection.sendall(http_response)
        client_connection.close()
    except KeyboardInterrupt:
        break

print "Ending server"
