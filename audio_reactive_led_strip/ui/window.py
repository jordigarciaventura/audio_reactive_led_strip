# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/9EFCFAC2FCFA93AD/Users/jordigv/Documents/Audio Reactive LED Strip/audio_reactive_led_strip/audio_reactive_led_strip/ui/window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(993, 624)
        self.gridLayout = QtWidgets.QGridLayout(Window)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Window)
        self.frame.setMinimumSize(QtCore.QSize(320, 0))
        self.frame.setMaximumSize(QtCore.QSize(320, 16777215))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(24, 24, 24, 4)
        self.verticalLayout_4.setSpacing(24)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(24)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sourceComboBox = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceComboBox.sizePolicy().hasHeightForWidth())
        self.sourceComboBox.setSizePolicy(sizePolicy)
        self.sourceComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.sourceComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.sourceComboBox.setFont(font)
        self.sourceComboBox.setObjectName("sourceComboBox")
        self.sourceComboBox.addItem("")
        self.horizontalLayout.addWidget(self.sourceComboBox)
        self.sourceButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceButton.sizePolicy().hasHeightForWidth())
        self.sourceButton.setSizePolicy(sizePolicy)
        self.sourceButton.setMinimumSize(QtCore.QSize(30, 30))
        self.sourceButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.sourceButton.setFont(font)
        self.sourceButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sourceButton.setIcon(icon)
        self.sourceButton.setIconSize(QtCore.QSize(18, 18))
        self.sourceButton.setObjectName("sourceButton")
        self.horizontalLayout.addWidget(self.sourceButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(0, 18))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.sensitivitySlider = JumpSlider(self.frame)
        self.sensitivitySlider.setMinimumSize(QtCore.QSize(0, 30))
        self.sensitivitySlider.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("STIXGeneral")
        self.sensitivitySlider.setFont(font)
        self.sensitivitySlider.setMinimum(1)
        self.sensitivitySlider.setMaximum(100)
        self.sensitivitySlider.setProperty("value", 100)
        self.sensitivitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.sensitivitySlider.setObjectName("sensitivitySlider")
        self.verticalLayout_5.addWidget(self.sensitivitySlider)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_8)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setSpacing(24)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.effectLabel = QtWidgets.QLabel(self.frame)
        self.effectLabel.setMinimumSize(QtCore.QSize(0, 18))
        self.effectLabel.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.effectLabel.setFont(font)
        self.effectLabel.setObjectName("effectLabel")
        self.verticalLayout_9.addWidget(self.effectLabel)
        self.effectComboBox = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.effectComboBox.sizePolicy().hasHeightForWidth())
        self.effectComboBox.setSizePolicy(sizePolicy)
        self.effectComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.effectComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.effectComboBox.setFont(font)
        self.effectComboBox.setObjectName("effectComboBox")
        self.verticalLayout_9.addWidget(self.effectComboBox)
        self.verticalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.intensityLabel = QtWidgets.QLabel(self.frame)
        self.intensityLabel.setMinimumSize(QtCore.QSize(0, 18))
        self.intensityLabel.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.intensityLabel.setFont(font)
        self.intensityLabel.setObjectName("intensityLabel")
        self.verticalLayout_6.addWidget(self.intensityLabel)
        self.intensitySlider = JumpSlider(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intensitySlider.sizePolicy().hasHeightForWidth())
        self.intensitySlider.setSizePolicy(sizePolicy)
        self.intensitySlider.setMinimumSize(QtCore.QSize(0, 30))
        self.intensitySlider.setMaximumSize(QtCore.QSize(16777215, 30))
        self.intensitySlider.setMinimum(0)
        self.intensitySlider.setMaximum(100)
        self.intensitySlider.setSingleStep(1)
        self.intensitySlider.setProperty("value", 100)
        self.intensitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.intensitySlider.setObjectName("intensitySlider")
        self.verticalLayout_6.addWidget(self.intensitySlider)
        self.verticalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 18))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addressLineEdit = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addressLineEdit.sizePolicy().hasHeightForWidth())
        self.addressLineEdit.setSizePolicy(sizePolicy)
        self.addressLineEdit.setMinimumSize(QtCore.QSize(150, 30))
        self.addressLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.addressLineEdit.setFont(font)
        self.addressLineEdit.setAccessibleName("")
        self.addressLineEdit.setText("")
        self.addressLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.horizontalLayout_2.addWidget(self.addressLineEdit)
        self.portLineEdit = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy)
        self.portLineEdit.setMinimumSize(QtCore.QSize(100, 30))
        self.portLineEdit.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.portLineEdit.setFont(font)
        self.portLineEdit.setText("")
        self.portLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.portLineEdit.setDragEnabled(False)
        self.portLineEdit.setObjectName("portLineEdit")
        self.horizontalLayout_2.addWidget(self.portLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.connectionCheckBox = QtWidgets.QCheckBox(self.frame)
        self.connectionCheckBox.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.connectionCheckBox.setFont(font)
        self.connectionCheckBox.setIconSize(QtCore.QSize(30, 30))
        self.connectionCheckBox.setObjectName("connectionCheckBox")
        self.verticalLayout.addWidget(self.connectionCheckBox)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.fpsLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fpsLabel.sizePolicy().hasHeightForWidth())
        self.fpsLabel.setSizePolicy(sizePolicy)
        self.fpsLabel.setMinimumSize(QtCore.QSize(0, 18))
        self.fpsLabel.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.fpsLabel.setFont(font)
        self.fpsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fpsLabel.setObjectName("fpsLabel")
        self.horizontalLayout_3.addWidget(self.fpsLabel)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 18))
        self.label.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter_2 = QtWidgets.QSplitter(Window)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setHandleWidth(6)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.pressurePlot = ReadOnlyPlot(self.splitter)
        self.pressurePlot.setObjectName("pressurePlot")
        self.frequencyPlot = ReadOnlyPlot(self.splitter)
        self.frequencyPlot.setObjectName("frequencyPlot")
        self.dbPlot = ReadOnlyPlot(self.splitter)
        self.dbPlot.setMinimumSize(QtCore.QSize(40, 0))
        self.dbPlot.setMaximumSize(QtCore.QSize(40, 16777215))
        self.dbPlot.setObjectName("dbPlot")
        self.rgbPlot = ReadOnlyPlot(self.splitter_2)
        self.rgbPlot.setObjectName("rgbPlot")
        self.verticalLayout_7.addWidget(self.splitter_2)
        self.previewView = QtWidgets.QGraphicsView(Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewView.sizePolicy().hasHeightForWidth())
        self.previewView.setSizePolicy(sizePolicy)
        self.previewView.setMinimumSize(QtCore.QSize(0, 30))
        self.previewView.setMaximumSize(QtCore.QSize(16777215, 30))
        self.previewView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.previewView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.previewView.setInteractive(True)
        self.previewView.setObjectName("previewView")
        self.verticalLayout_7.addWidget(self.previewView)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 1, 1, 1)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Reactive LED Strip"))
        self.label_2.setText(_translate("Window", "Source"))
        self.sourceComboBox.setItemText(0, _translate("Window", "-- No source --"))
        self.label_3.setText(_translate("Window", "Sensitivity"))
        self.effectLabel.setText(_translate("Window", "Effect"))
        self.intensityLabel.setText(_translate("Window", "Intensity"))
        self.label_4.setText(_translate("Window", "Connection"))
        self.addressLineEdit.setPlaceholderText(_translate("Window", "address"))
        self.portLineEdit.setPlaceholderText(_translate("Window", "port"))
        self.connectionCheckBox.setText(_translate("Window", "Send"))
        self.fpsLabel.setText(_translate("Window", "60"))
        self.label.setText(_translate("Window", "FPS"))
from widgets import JumpSlider, ReadOnlyPlot
import resources_rc
