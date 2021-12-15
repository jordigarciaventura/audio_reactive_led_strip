"""This module provides the Reactive LED Strip application."""

import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu

from .view import Window
from .controller import Controller
from .recorder import AudioStream
from . import config
from .ui import resources_rc
from PyQt5.QtGui import QIcon
    
def main():
    # Create the application
    app = QApplication(["Reactive LED Strip"])
    app.setQuitOnLastWindowClosed(False)

    app.setWindowIcon(QIcon(":/icons/icon.ico"))
    
    # Add stylesheet
    dirname = os.path.dirname(__file__)
    stylesheetPath = os.path.join(dirname, "ui", "stylesheet.qss")
    
    with open(stylesheetPath) as f:
        app.setStyleSheet(f.read())

    # Create and show the main window
    win = Window()
    win.show()

    recorder = AudioStream( samplerate=config.MIC_RATE,
                            numframes=config.SAMPLES_PER_FRAME, 
                            blocksize=config.SAMPLES_PER_FRAME)
    controller = Controller(recorder, win)

    # Close

    def quitApplicattion():
        app.exit()

    def onCloseEvent():
        if controller.send:
            win.hide()
        else:
            quitApplicattion()

    win.onCloseEvent(onCloseEvent)

    # Show
    def showWindow():
        win.show()


    # Tray
    tray = QSystemTrayIcon()

    trayMenu = QMenu()
    trayOpen = trayMenu.addAction("&Open")
    trayOpen.triggered.connect(showWindow)
    trayExit = trayMenu.addAction("E&xit")
    trayExit.triggered.connect(quitApplicattion)
    tray.setContextMenu(trayMenu)

    tray.setIcon(QIcon(":/icons/icon.ico"))
    tray.show()
        

    # Run the event loop
    p = app.exec()

    recorder.exit()

    sys.exit(p)