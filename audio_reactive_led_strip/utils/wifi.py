import socket
import numpy as np


class Connection():
    def __init__(self, address="192.168.1.133", port=8888):
        self.address = address
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, r, g, b):
        if self.address and self.port:
            data = np.column_stack(
                [r, g, b]).flatten().astype(np.uint8).tobytes()
            try:
                self.s.sendto(data, (self.address, self.port))
            except:
                pass


if "__name__" == "__main__":
    connection = Connection("192.168.1.133", 8888)
    r = np.full(60, 255)
    g = np.full(60, 128)
    b = np.full(60, 0)
    connection.send(r, g, b)
