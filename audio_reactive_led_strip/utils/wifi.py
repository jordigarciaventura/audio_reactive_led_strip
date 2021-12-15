import socket
import numpy as np

class Connection():
    def __init__(self, address="192.168.2.1", port=2020):
        self.address = address
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, r, g, b):
        if self.address and self.port:
            data = np.column_stack([r, g, b]).flatten().astype(np.uint8).tobytes()
            try:
                self.s.sendto(data, (self.address, self.port))
            except:
                pass