"""This module provides the Reactive LED Strip main window."""

from .ui.window import Ui_Window

from PyQt5.QtWidgets import QWidget, QGraphicsScene, QMainWindow
from PyQt5.QtGui import QGradient, QValidator, QBrush, QLinearGradient, QColor
from pyqtgraph import PlotWidget, AxisItem, BarGraphItem
from PyQt5.QtCore import QSize, QEvent, Qt

from . import config
from . import recorder
from .audio import AudioVisualizer

import re
import numpy as np

class RangeValidator(QValidator):
    def __init__(self, min, max):
        super().__init__()
        self.min = min
        self.max = max

    def validate(self, text, pos):
        if not text:
            return(QValidator.Acceptable, text, pos)

        try:
            value = int(text)
        except:
            return(QValidator.Invalid, text, pos)

        if self.min <= value and value <= self.max:
            return (QValidator.Acceptable, text, pos)
        else:
            return(QValidator.Invalid, text, pos)

class Window(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self._setupUI()
        self.i = 0

        self.minimized = False
        self._activated = False

    def closeEvent(self, event):
        self.callbackOnClose()


    def onCloseEvent(self, callback):
        self.callbackOnClose = callback

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() and self.windowState() == Qt.WindowMinimized:
                self.minimized = True
                self._activated = False
        elif event.type() == QEvent.ActivationChange:
            if not self._activated:
                self._activated = True
            elif self.minimized:
                self.minimized = False

    def _setupUI(self):
        self.setupUi(self)
        self._setValidators()
        self.setSourceComboBox(recorder.getSourceNames())
        self.setFPSLabel(config.FPS)
        self.setEffectComboBox(AudioVisualizer.effectNames)
        self._initPlots()
        self.clearPlots()

    def _setValidators(self):
        self.portLineEdit.setValidator(RangeValidator(1, 65535))

    def setSourceComboBox(self, items):
        # clear all except default
        sourcesCount = self.sourceComboBox.count()
        for _ in range(sourcesCount-1):
            self.sourceComboBox.removeItem(1)
        self.sourceComboBox.addItems(items)

    def setEffectComboBox(self, items):
        self.effectComboBox.clear()
        self.effectComboBox.addItems(items)

    def setFPSLabel(self, fps):
        self.fpsLabel.setText(str(fps))

    def getAddress(self):
        return self.addressLineEdit.text()

    def getPort(self):
        return self.portLineEdit.text()

    def getEffectName(self):
        return self.effectComboBox.currentText()

    # INIT

    def _initPlots(self):
        self._initPressurePlot()
        self._initFrequencyPlot()
        self._initDbPlot()
        self._initRGBPlot()
        self._initPreviewView()

    def _initPressurePlot(self):

        self.pressurePlot.setTitle("Pressure")
        self.pressurePlot.setRange(xRange=(0, config.SAMPLES_PER_FRAME), yRange=(-1,1))
        x = [0, config.SAMPLES_PER_FRAME]
        ax = AxisItem(orientation="bottom")
        ax.setTicks([[(v, str(v)) for v in x]])
        y = [-1, 0, 1]
        ay = AxisItem(orientation="left")
        ay.setTicks([[(v, str(v)) for v in y]])
        self.pressurePlot.setAxisItems({"bottom": ax, "left": ay})
        self._pressureCurve = self.pressurePlot.plot(pen="y")
        
    def _initFrequencyPlot(self):
        self.frequencyPlot.setTitle("Frequency")
        self.frequencyPlot.setRange(xRange=(config.MIN_FREQUENCY, config.MAX_FREQUENCY), yRange=(0,1.2))
        x = [config.MIN_FREQUENCY, config.MAX_FREQUENCY]
        ax = AxisItem(orientation="bottom")
        ax.setTicks([[(v, str(v)) for v in x]])
        y = [0, 1.2]
        ay = AxisItem(orientation="left")
        ay.setTicks([[(v, str(v)) for v in y]])
        self.frequencyPlot.setAxisItems({"bottom": ax, "left": ay})
        self._frequencyCurve = self.frequencyPlot.plot(pen="y")

    def _initDbPlot(self):
        self.dbPlot.setTitle("dB")
        self.dbPlot.setRange(xRange=(0,0), yRange=(0,1))
        self.dbPlot.setMouseEnabled(x=False, y=False)
        ax = AxisItem(orientation="bottom")
        ax.setTicks([[(0,"0")]])
        self.dbPlot.setAxisItems({"bottom": ax})
        self.dbPlot.hideAxis("left")

        self._dbBar = BarGraphItem(x=[0], height = 0, width=1, pen='g', brush='g')

        self.dbPlot.addItem(self._dbBar)

    def _initRGBPlot(self):
        self.rgbPlot.setTitle("RGB")
        self.rgbPlot.setRange(xRange=(0, config.N_PIXELS), yRange=(0,255))
        x = [0, config.N_PIXELS]
        ax = AxisItem(orientation="bottom")
        ax.setTicks([[(v, str(v)) for v in x]])
        self.rgbPlot.setAxisItems({"bottom": ax})
        self.rgbPlot.hideAxis("left")
        self._rCurve = self.rgbPlot.plot(pen="r")
        self._gCurve = self.rgbPlot.plot(pen="g")
        self._bCurve = self.rgbPlot.plot(pen="b")

    def _initPreviewView(self):
        previewScene = QGraphicsScene()
        self.previewView.setScene(previewScene)
        self.clearPreview()

    # DRAW

    def drawPressure(self, data):
        self._pressureCurve.setData(data)

    def drawFrequency(self, data):
        self._frequencyCurve.setData(*data)

    def drawRGB(self, r, g, b):
        self._rCurve.setData(r)
        self._gCurve.setData(g)
        self._bCurve.setData(b)

    def drawPreview(self, colors):
        leds = len(colors)

        if leds == 0: return

        width = 1/leds
        start = width/2

        gradient = QLinearGradient()
        gradient.setCoordinateMode(QGradient.ObjectMode)
        gradient.setStart(0,0)
        gradient.setFinalStop(1,0)

        for i in range(leds):
            r, g, b = colors[i]
            color = QColor(int(r), int(g), int(b))
            pos = start + width * i
            gradient.setColorAt(pos, color)
        
        brush = QBrush(gradient)
        self.previewView.setBackgroundBrush(brush)

    def drawDb(self, db):
        self._dbBar.setOpts(height=db)

    # CLEAR

    def clearPlots(self):
        self.clearPressure()
        self.clearFrequency()
        self.clearPreview()
        self.clearRGB()
        self.clearDb()

    def clearPressure(self):
        self.drawPressure(np.zeros(config.SAMPLES_PER_FRAME))

    def clearFrequency(self):
        x = np.linspace(config.MIN_FREQUENCY, config.MAX_FREQUENCY, config.N_FFT_BINS)
        y = np.zeros(config.N_FFT_BINS)
        self.drawFrequency((x,y))

    def clearPreview(self):
        black = np.zeros((config.N_PIXELS, 3))
        self.drawPreview(black)

    def clearDb(self):
        self.drawDb(0)

    def clearRGB(self):
        black = np.zeros((3, config.N_PIXELS))
        self.drawRGB(*black)