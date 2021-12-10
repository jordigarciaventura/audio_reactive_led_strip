# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/9EFCFAC2FCFA93AD/Users/jordigv/Documents/Audio Reactive LED Strip/project/reactive_led_strip/ui/window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(525, 788)
        self.gridLayout = QtWidgets.QGridLayout(Window)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.outputGroup = QtWidgets.QGroupBox(Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputGroup.sizePolicy().hasHeightForWidth())
        self.outputGroup.setSizePolicy(sizePolicy)
        self.outputGroup.setMinimumSize(QtCore.QSize(0, 250))
        self.outputGroup.setAutoFillBackground(False)
        self.outputGroup.setObjectName("outputGroup")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.outputGroup)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.outputLayout = QtWidgets.QVBoxLayout()
        self.outputLayout.setSpacing(0)
        self.outputLayout.setObjectName("outputLayout")
        self.previewView = QtWidgets.QGraphicsView(self.outputGroup)
        self.previewView.setMinimumSize(QtCore.QSize(0, 30))
        self.previewView.setMaximumSize(QtCore.QSize(16777215, 30))
        self.previewView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.previewView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.previewView.setInteractive(True)
        self.previewView.setObjectName("previewView")
        self.outputLayout.addWidget(self.previewView)
        self.verticalLayout_3.addLayout(self.outputLayout)
        self.gridLayout.addWidget(self.outputGroup, 6, 0, 1, 1)
        self.sourceGroup = QtWidgets.QGroupBox(Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceGroup.sizePolicy().hasHeightForWidth())
        self.sourceGroup.setSizePolicy(sizePolicy)
        self.sourceGroup.setFlat(False)
        self.sourceGroup.setCheckable(False)
        self.sourceGroup.setObjectName("sourceGroup")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sourceGroup)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sourceComboBox = QtWidgets.QComboBox(self.sourceGroup)
        self.sourceComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.sourceComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.sourceComboBox.setObjectName("sourceComboBox")
        self.sourceComboBox.addItem("")
        self.horizontalLayout.addWidget(self.sourceComboBox)
        self.sourceButton = QtWidgets.QPushButton(self.sourceGroup)
        self.sourceButton.setMinimumSize(QtCore.QSize(100, 30))
        self.sourceButton.setMaximumSize(QtCore.QSize(100, 30))
        self.sourceButton.setObjectName("sourceButton")
        self.horizontalLayout.addWidget(self.sourceButton)
        self.gridLayout.addWidget(self.sourceGroup, 1, 0, 1, 1)
        self.connectionGroup = QtWidgets.QGroupBox(Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectionGroup.sizePolicy().hasHeightForWidth())
        self.connectionGroup.setSizePolicy(sizePolicy)
        self.connectionGroup.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.connectionGroup.setObjectName("connectionGroup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.connectionGroup)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ipLineEdit = QtWidgets.QLineEdit(self.connectionGroup)
        self.ipLineEdit.setMinimumSize(QtCore.QSize(150, 30))
        self.ipLineEdit.setMaximumSize(QtCore.QSize(150, 28))
        self.ipLineEdit.setAccessibleName("")
        self.ipLineEdit.setText("")
        self.ipLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.horizontalLayout_2.addWidget(self.ipLineEdit)
        self.portLineEdit = QtWidgets.QLineEdit(self.connectionGroup)
        self.portLineEdit.setMinimumSize(QtCore.QSize(100, 30))
        self.portLineEdit.setMaximumSize(QtCore.QSize(100, 28))
        self.portLineEdit.setText("")
        self.portLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.portLineEdit.setDragEnabled(False)
        self.portLineEdit.setObjectName("portLineEdit")
        self.horizontalLayout_2.addWidget(self.portLineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.connectionCheckBox = QtWidgets.QCheckBox(self.connectionGroup)
        self.connectionCheckBox.setObjectName("connectionCheckBox")
        self.horizontalLayout_2.addWidget(self.connectionCheckBox)
        self.gridLayout.addWidget(self.connectionGroup, 8, 0, 1, 1)
        self.effectGroup = QtWidgets.QGroupBox(Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.effectGroup.sizePolicy().hasHeightForWidth())
        self.effectGroup.setSizePolicy(sizePolicy)
        self.effectGroup.setObjectName("effectGroup")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.effectGroup)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.effectComboBox = QtWidgets.QComboBox(self.effectGroup)
        self.effectComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.effectComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.effectComboBox.setObjectName("effectComboBox")
        self.horizontalLayout_3.addWidget(self.effectComboBox)
        self.effectToolButton = QtWidgets.QToolButton(self.effectGroup)
        self.effectToolButton.setMinimumSize(QtCore.QSize(30, 30))
        self.effectToolButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.effectToolButton.setObjectName("effectToolButton")
        self.horizontalLayout_3.addWidget(self.effectToolButton)
        self.gridLayout.addWidget(self.effectGroup, 3, 0, 1, 1)
        self.inputGroup = QtWidgets.QGroupBox(Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputGroup.sizePolicy().hasHeightForWidth())
        self.inputGroup.setSizePolicy(sizePolicy)
        self.inputGroup.setMinimumSize(QtCore.QSize(0, 250))
        self.inputGroup.setMaximumSize(QtCore.QSize(16777215, 250))
        self.inputGroup.setCheckable(False)
        self.inputGroup.setObjectName("inputGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.inputGroup)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputSplitter = QtWidgets.QSplitter(self.inputGroup)
        self.inputSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.inputSplitter.setHandleWidth(1)
        self.inputSplitter.setObjectName("inputSplitter")
        self.verticalLayout_2.addWidget(self.inputSplitter)
        self.gridLayout.addWidget(self.inputGroup, 2, 0, 1, 1)
        self.fpsLayout = QtWidgets.QHBoxLayout()
        self.fpsLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.fpsLayout.setContentsMargins(0, 0, 0, 0)
        self.fpsLayout.setSpacing(6)
        self.fpsLayout.setObjectName("fpsLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.fpsLayout.addItem(spacerItem1)
        self.fpsLabel = QtWidgets.QLabel(Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fpsLabel.sizePolicy().hasHeightForWidth())
        self.fpsLabel.setSizePolicy(sizePolicy)
        self.fpsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fpsLabel.setObjectName("fpsLabel")
        self.fpsLayout.addWidget(self.fpsLabel)
        self.label = QtWidgets.QLabel(Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.fpsLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.fpsLayout, 7, 0, 1, 1)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
        Window.setTabOrder(self.ipLineEdit, self.portLineEdit)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Reactive LED Strip"))
        self.outputGroup.setTitle(_translate("Window", "Output"))
        self.sourceGroup.setTitle(_translate("Window", "Source"))
        self.sourceComboBox.setItemText(0, _translate("Window", "-- No source --"))
        self.sourceButton.setText(_translate("Window", "Refresh"))
        self.connectionGroup.setTitle(_translate("Window", "Connection"))
        self.ipLineEdit.setPlaceholderText(_translate("Window", "IP"))
        self.portLineEdit.setPlaceholderText(_translate("Window", "port"))
        self.connectionCheckBox.setText(_translate("Window", "Send"))
        self.effectGroup.setTitle(_translate("Window", "Effect"))
        self.effectToolButton.setText(_translate("Window", "..."))
        self.inputGroup.setTitle(_translate("Window", "Input"))
        self.fpsLabel.setText(_translate("Window", "60"))
        self.label.setText(_translate("Window", "FPS"))