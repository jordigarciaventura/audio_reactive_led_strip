import sys
import os

import warnings
warnings.simplefilter("ignore", UserWarning)

from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon

from .common.view import Window
from .common.controller import Controller
from .utils.recorder import AudioStream
from .common import config
from .resources import resources_rc

def main():
    # Create application
    app = QApplication(["Reactive LED Strip"])
    app.setWindowIcon(QIcon(":/icons/icon.ico"))
    app.setQuitOnLastWindowClosed(False)

    # Add stylesheet
    dirname = os.path.dirname(__file__)
    stylesheetPath = os.path.join(dirname, "gui", "stylesheet.qss")

    with open(stylesheetPath) as f:
        app.setStyleSheet(f.read())

    # Create and show the main window
    win = Window()
    win.show()
    recorder = AudioStream(samplerate=config.MIC_RATE,
                           numframes=config.SAMPLES_PER_FRAME,
                           blocksize=config.SAMPLES_PER_FRAME)
    controller = Controller(recorder, win)

    # Close event
    def onCloseEvent():
        if controller.send:
            win.hide()
        else:
            app.exit()

    win.onCloseEvent(onCloseEvent)

    # System Tray
    tray = QSystemTrayIcon()
    tray.setIcon(QIcon(":/icons/icon.ico"))

    trayMenu = QMenu()

    trayOpen = trayMenu.addAction("&Open")
    trayOpen.triggered.connect(lambda: win.show())

    trayExit = trayMenu.addAction("E&xit")
    trayExit.triggered.connect(lambda: app.exit())

    tray.setContextMenu(trayMenu)

    tray.show()

    # Run the event loop
    p = app.exec()

    # Finalization
    recorder.exit()

    sys.exit(p)
