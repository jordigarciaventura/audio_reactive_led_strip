from PyQt5.QtWidgets import QSlider, QStyle
from pyqtgraph import PlotWidget


class JumpSlider(QSlider):

    selected = False

    def mousePressEvent(self, ev):
        """ Jump to click position """
        self.setValue(QStyle.sliderValueFromPosition(
            self.minimum(), self.maximum(), ev.x(), self.width()))
        self.selected = True

    def mouseReleaseEvent(self, ev):
        """ Jump to click position """
        self.selected = False

    def mouseMoveEvent(self, ev):
        """ Jump to pointer position while moving """
        if self.selected:
            self.setValue(QStyle.sliderValueFromPosition(
                self.minimum(), self.maximum(), ev.x(), self.width()))


class ReadOnlyPlot(PlotWidget):

    def __init__(self, *kargs):
        super().__init__(enableMenu=False, *kargs)
        self.hideButtons()
        self.disableAutoRange()
        self.setMouseEnabled(x=False, y=False)
