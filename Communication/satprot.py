from socket import socket

class InMsg():

    def __init__(self, body, offset = 0):
        self.body = body
        self.ptr = 2 + offset
        self.type = body[0 + offset]
        self.status = body[1 + offset]

    def get_type(self):
        return self.type

    def get_status(self):
        return self.status

    def next_int(self):
        