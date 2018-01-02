import config
import socket

soc = socket.socket()
soc.bind(("",config.HTTP_PORT))
soc.close()