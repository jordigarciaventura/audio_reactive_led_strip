from PyQt5.QtCore import QTimer

from . import config
from . import recorder
from . import audio
from . import wifi
from .fps import FPSMeter

import numpy as np

class Controller():
    def __init__(self, recorder, view):
        self._view = view
        self._recorder = recorder
        
        self._fpsMeter = FPSMeter(config.FPS, self._view.setFPSLabel)
        self._sensitivity = 1

        self.db = audio.DBMeter(decrement=0.05)
        self._audioVisualizer = audio.AudioVisualizer(n_samples=config.SAMPLES_PER_FRAME)

        self._connection = wifi.Connection()
        self._send = False

        self._connectSignals()

    def _connectSignals(self):
        self._view.sourceButton.clicked.connect(self._updateSourceComboBox)
        self._view.sourceComboBox.currentIndexChanged.connect(self._setSourceIndex)
        self._view.pressurePlot.onMouseWheelDown(self._decreaseSensitivity)
        self._view.pressurePlot.onMouseWheelUp(self._increaseSensitivity)
        self._view.effectComboBox.currentIndexChanged.connect(self._setEffect)
        self._view.intensitySlider.valueChanged.connect(self._setIntensity)
        self._view.addressLineEdit.editingFinished.connect(self._setAddress)
        self._view.portLineEdit.editingFinished.connect(self._setPort)
        self._view.connectionCheckBox.stateChanged.connect(self._setConnection)

    def _updateSourceComboBox(self):
        self._view.setSourceComboBox(recorder.getSourceNames())

    def _setSourceIndex(self, index):
        if index == 0:
            self._stop()
        else:
            self._recorder.update(index=index-1)
            self._start()

    def _decreaseSensitivity(self):
        self._sensitivity /= 1.2

    def _increaseSensitivity(self):
        self._sensitivity *= 1.2 

    def _setEffect(self):
        effectName = self._view.getEffectName()
        self._audioVisualizer.setEffect(effectName)

    def _setIntensity(self, intensity):
        self._audioVisualizer.intensity = intensity/100

    def _setAddress(self):
        self._connection.address = self._view.getAddress()

    def _setPort(self):
        port = self._view.getPort()
        if port:
            port = int(port)
        self._connection.port = port

    def _setConnection(self, state):
        self._send = state != 0

    def _start(self):
        self._recorder.start()

        self._fpsMeter.start()

        self._timer = QTimer()
        self._timer.setInterval(1000//config.FPS)
        self._timer.timeout.connect(self._routine)
        self._timer.start()

    def _stop(self):
        self._recorder.stop()
        self._timer.stop()
        self._view.clearPlots()

    def _routine(self):
        if self._recorder.hasNewAudio:
            data = self._recorder.data
            data *= self._sensitivity
            self._audioVisualizer.setData(data)

            if not self._view.minimized:
                self._drawPlots()

            if self._send:
                self._sendData()
        
        self._fpsMeter.update()

    def _drawPlots(self):

        self._drawPressure(self._audioVisualizer.data)
        self._drawDb(self._audioVisualizer.data)

        self._drawFrequency()
        self._drawRGB()
        self._drawPreview()

    def _drawPressure(self, data):
        self._view.drawPressure(data)

    def _drawFrequency(self):
        x, y = self._audioVisualizer.frequency()
        self._view.drawFrequency((x, y))

    def _drawRGB(self):
        r, g, b = self._audioVisualizer.getRGB()
        self._view.drawRGB(r, g, b)

    def _drawDb(self, data):
        dbValue = self.db.update(data)
        self._view.drawDb(dbValue)

    def _drawPreview(self):
        r, g, b = self._audioVisualizer.getRGB()
        self._view.drawPreview(list(zip(r, g, b)))

    def _sendData(self):
        r, g, b = self._audioVisualizer.getRGB()
        self._connection.send(r, g, b)