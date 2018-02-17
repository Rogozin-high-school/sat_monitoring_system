import threading
import json

class Communications(threading.Thread):
    def __init__(self, command_handler):
        threading.Thread.__init__(self)
        self.should_run = True
        self.command_handler = command_handler

   
    # Starts handling http requests
    def run(self):
        
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind((config.HTTP_HOST, config.HTTP_PORT))
        listen_socket.listen(1)
        
        print("Starting communications module")
        
        while self.should_run:
            client_connection, client_address = listen_socket.accept()
            request = client_connection.recv(1024)
            
            request_split = str(request).split(' ')
            if len(request_split) <= 1:
                # Probably not an HTTP packet or something like that
                continue

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

            # Adding HTTP headers
            http_response = "HTTP/1.1 200 OK\n"
            http_response += "Content-Type: text/html\n"
            http_response += "Connection: close\n"
            http_response += "\n"
       
            # Finding matching command handler on the command handlers file
            if hasattr(self.command_handler, path):
                command_handler = getattr(self.command_handler, path)
                http_response += command_handler(parameters)
            else:
                http_response += "Command not found"

            # Sending a response and closing the connection
            client_connection.sendall(http_response.encode())
            client_connection.close()

    # Stops the communications module
    def stop(self):
        self.should_run = False
