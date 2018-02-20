from socket import socket
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
        self.soc = socket()
        self.ip = ip
        self.port = port
        self.soc.connect((ip, port))

    def send(self, msg : OutMsg):
        self.soc.send(msg.get_bytes())

    def recv(self) -> InMsg:
        l = sum(struct.unpack("I", self.soc.recv(4)))
        print("Length " + str(l))
        return InMsg(self.soc.recv(l))

    def close(self):
        self.soc.close()

c = Connection("localhost", 8080)
m = OutMsg(5, 4)
m.add_int(2)
c.send(m)

x = c.recv()
