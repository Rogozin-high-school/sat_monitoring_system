from socket import *
import struct

class InMsg(object):

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
        data = self.body[self.ptr : self.ptr + 4]
        self.ptr += 4
        data = sum(struct.unpack("I", bytearray(data)))
        return data

    def next_float(self):
        data = self.body[self.ptr : self.ptr + 4]
        self.ptr += 4
        data = sum(struct.unpack("f", bytearray(data)))
        return data

class OutMsg(object):
    def __init__(self, _type, status):
        self.type = _type
        self.status = status
        self.params = []
    
    def add_int(self, i):
        self.params.append(struct.pack("I", i))

    def add_float(self, f):
        self.params.append(struct.pack("f", f))

    def get_bytes(self):
        body = bytes()
        for x in self.params:
            body += x
        body = struct.pack("I", len(body) + 2) + bytes([self.type, self.status]) + body
        return body

class Connection(object):
    def __init__(self, ip, port):
        self.soc = socket(AF_INET, SOCK_DGRAM)
        self.soc.settimeout(1)
        self.ip = ip
        self.port = port

    def send(self, msg : OutMsg):
        self.soc.sendto(msg.get_bytes(), (self.ip, self.port))