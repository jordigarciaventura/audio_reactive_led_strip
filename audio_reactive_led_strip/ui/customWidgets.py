from PyQt5 import QtWidgets

class JumpSlider(QtWidgets.QSlider):

    selected = False

    def mousePressEvent(self, ev):
        """ Jump to click position """
        self.setValue(QtWidgets.QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), ev.x(), self.width()))
        self.selected = True

    def mouseReleaseEvent(self, ev):
        """ Jump to click position """
        self.selected = False

    def mouseMoveEvent(self, ev):
        """ Jump to pointer position while moving """
        if self.selected:
            self.setValue(QtWidgets.QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), ev.x(), self.width()))