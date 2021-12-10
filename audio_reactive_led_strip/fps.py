import time

from . import config

class FPSMeter():
    def __init__(self, fps, callback):
        self.fps = fps
        self.callback = callback

    def start(self):
        self.start_time = time.time()
        self.frames = 0

    def update(self):
        self.frames += 1
        if self.frames == self.fps:
            fps = int(self.fps/(time.time()- self.start_time))
            self.callback(fps)
            self.start()