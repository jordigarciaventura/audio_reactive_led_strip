import soundcard as sc
import threading

class AudioStream():
    def __init__(self, samplerate=44100, channels=1, blocksize=1024, numframes=1024, index=0):
        self.samplerate = samplerate
        self.channels = channels
        self.blocksize = blocksize
        self.numframes = numframes
        self.index = index
        
        self.hasNewAudio = False
        self._requiresUpdate = False
        self._paused = True
        self._stopped = False
        self._started = False

    def start(self):
        if not self._started:
            self._thread = threading.Thread(target=self._record)
            self._thread.start()
            self._started = True

        self._paused = False
        self._requiresUpdate = True

    def stop(self):
        self._paused = True
        self._requiresUpdate = True

    def exit(self):
        if self._started:
            self._stopped = True
            self._requiresUpdate = True
            self._thread.join()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key == "samplerate":
                self.samplerate = value
            elif key == "channels":
                self.channels = value
            elif key == "blocksize":
                self.blocksize = value
            elif key == "numframes":
                self.numframes = value
            elif key == "index":
                self.index = value

        self._requiresUpdate = True

    def _record(self):
        while not self._stopped:
            if not self._paused:
                source = sc.all_microphones(True)[self.index]
                with source.recorder(self.samplerate, self.channels, self.blocksize) as recorder:
                    while not self._requiresUpdate:
                        self._data = recorder.record(self.numframes).flatten()
                        self.hasNewAudio = True
                self._requiresUpdate = False

    @property
    def data(self):
        """Get the ring buffer."""
        self.hasNewAudio = False
        return self._data

def getSourceNames():
    sources = sc.all_microphones(True)
    return [source.name for source in sources]