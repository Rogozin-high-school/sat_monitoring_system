# ------------ import statements
import socket
import hmc5883l

# ------------ variables
HOST, PORT = '', 8080
magnetometer = hmc5883l.hmc5883l()

# ------------ methods
# TODO : Implement this methods
# returns the current x magnetometer reading
def GetX():
    return 'X'

# returns the current y magnetometer reading
def GetY():
    return 'Y'

# returns the current z magnetometer reading
def GetZ():
    return 'Z'


# ------------ main code
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
