import socket
import numpy as np

class Connection():
    def __init__(self, ip="192.168.2.1", port=2020):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, r, g, b):
        data = np.concatenate([r, g, b]).astype(np.uint8).tobytes()
        self.s.sendto(data, (self.ip, self.port))