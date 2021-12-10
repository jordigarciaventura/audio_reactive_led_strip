"""This module provides the Reactive LED Strip application."""

import sys

from PyQt5.QtWidgets import QApplication

from .view import Window
from .controller import Controller
from .recorder import AudioStream
from . import config

def main():
    # Create the application
    app = QApplication([])
    # Create and show the main window
    win = Window()
    win.show()

    recorder = AudioStream( samplerate=config.MIC_RATE,
                            numframes=config.SAMPLES_PER_FRAME, 
                            blocksize=config.SAMPLES_PER_FRAME)
    Controller(recorder, win)

    # Run the event loop
    p = app.exec()

    recorder.exit()

    sys.exit(p)