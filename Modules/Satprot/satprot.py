from socket import *
import struct

class InMsg(object):
    """
    A message parser for incoming byte-arrays.
    Converts connection messages to message objects.
    """
    def __init__(self, body : list, offset : int = 0):
        """
        Initializes a new InMsg object.
        Parameters:
            body    - the byte array containing the body of the message.
            offset  - the offset of the message to start reading from.
                      First byte *(body+offset) is the type of the message.
        """
        self.body = body
        self.ptr = 2 + offset
        self.type = body[0 + offset]
        self.status = body[1 + offset]

    def get_type(self) -> int:
        """
        Returns the message type.
        """
        return self.type

    def get_status(self) -> int:
        """
        Returns the message satatus.
        """
        return self.status

    def next_int(self) -> int:
        """
        Reads the next parameter from the message as an integer number.
        """
        data = self.body[self.ptr : self.ptr + 4]
        self.ptr += 4
        data = sum(struct.unpack("I", bytearray(data)))
        return data

    def next_float(self) -> float:
        """
        Reads the next parameter from the message as a floating point number.
        """
        data = self.body[self.ptr : self.ptr + 4]
        self.ptr += 4
        data = sum(struct.unpack("f", bytearray(data)))
        return data

class OutMsg(object):
    """
    Constructs messages for sending, and converting message objects to byte arrays.
    """
    def __init__(self, _type : int, status : int):
        """
        Initializes a new OutMsg object.
        Parameters:
            type - the type of the message (single byte int), that will set the 
                    server's way of reacting to the message.
            status - the status of the message (single byte int), which is returned
                    by the server to indicate the result of the required action (if required).
        """
        self.type = _type
        self.status = status
        self.params = []
    
    def add_int(self, i : int):
        """
        Adds a new integer parameter to the stream.
        Parameters:
            i - the parameter to add.
        """
        self.params.append(struct.pack("I", i))

    def add_float(self, f : float):
        """
        Adds a new floating point parameter to the stream.
        Parameters:
            f - the parameter to add.
        """
        self.params.append(struct.pack("f", f))

    def get_bytes(self) -> list:
        """
        Gets the byte array encoding of the message. Returns as a list of integers.
        """
        body = bytes()
        for x in self.params:
            body += x
        body = struct.pack("I", len(body) + 2) + bytes([self.type, self.status]) + body
        return body

class Connection(object):
    """
    For connecting to services using UDP.
    """
    def __init__(self, ip : str, port : int):
        """
        Initializes a connection engine.
        Parmeters:
            ip - the ip (as a string) of the machine to connect to.
            port - the port to connect to.
        """
        self.soc = socket(AF_INET, SOCK_DGRAM)
        self.soc.settimeout(1)
        self.ip = ip
        self.port = port

    def send(self, msg : OutMsg):
        """
        Sends a message using the specified connection tunnel.
        Parameters:
            msg - an OutMsg object describing the message to be sent.
        """
        self.soc.sendto(msg.get_bytes(), (self.ip, self.port))