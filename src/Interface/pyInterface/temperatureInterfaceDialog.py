# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temperatureInterfaceDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_configurationPlotDialog(object):
    def setupUi(self, configurationPlotDialog):
        configurationPlotDialog.setObjectName("configurationPlotDialog")
        configurationPlotDialog.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(configurationPlotDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(configurationPlotDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 8, 0, 1, 1)
        self.plotTitleInputTemp = QtWidgets.QLineEdit(self.groupBox)
        self.plotTitleInputTemp.setObjectName("plotTitleInputTemp")
        self.gridLayout_2.addWidget(self.plotTitleInputTemp, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.plotStyleBox = QtWidgets.QComboBox(self.groupBox)
        self.plotStyleBox.setObjectName("plotStyleBox")
        self.plotStyleBox.addItem("")
        self.plotStyleBox.addItem("")
        self.plotStyleBox.addItem("")
        self.plotStyleBox.addItem("")
        self.plotStyleBox.addItem("")
        self.plotStyleBox.addItem("")
        self.gridLayout_2.addWidget(self.plotStyleBox, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.axisXInputTemp = QtWidgets.QLineEdit(self.groupBox)
        self.axisXInputTemp.setObjectName("axisXInputTemp")
        self.gridLayout_2.addWidget(self.axisXInputTemp, 5, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 2)
        self.axisYInputTemp = QtWidgets.QLineEdit(self.groupBox)
        self.axisYInputTemp.setObjectName("axisYInputTemp")
        self.gridLayout_2.addWidget(self.axisYInputTemp, 7, 0, 1, 2)
        self.fontsizeInputTemp = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontsizeInputTemp.sizePolicy().hasHeightForWidth())
        self.fontsizeInputTemp.setSizePolicy(sizePolicy)
        self.fontsizeInputTemp.setObjectName("fontsizeInputTemp")
        self.gridLayout_2.addWidget(self.fontsizeInputTemp, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.tempDialogButtonBox = QtWidgets.QDialogButtonBox(configurationPlotDialog)
        self.tempDialogButtonBox.setOrientation(QtCore.Qt.Vertical)
        self.tempDialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.tempDialogButtonBox.setObjectName("tempDialogButtonBox")
        self.horizontalLayout.addWidget(self.tempDialogButtonBox)

        self.retranslateUi(configurationPlotDialog)
        self.tempDialogButtonBox.accepted.connect(configurationPlotDialog.accept) # type: ignore
        self.tempDialogButtonBox.rejected.connect(configurationPlotDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(configurationPlotDialog)

    def retranslateUi(self, configurationPlotDialog):
        _translate = QtCore.QCoreApplication.translate
        configurationPlotDialog.setWindowTitle(_translate("configurationPlotDialog", "Dialog"))
        self.groupBox.setTitle(_translate("configurationPlotDialog", "Configure"))
        self.label_2.setText(_translate("configurationPlotDialog", "Plot Title"))
        self.label_5.setText(_translate("configurationPlotDialog", "Fontsize"))
        self.plotStyleBox.setItemText(0, _translate("configurationPlotDialog", "default"))
        self.plotStyleBox.setItemText(1, _translate("configurationPlotDialog", "classic"))
        self.plotStyleBox.setItemText(2, _translate("configurationPlotDialog", "bmh"))
        self.plotStyleBox.setItemText(3, _translate("configurationPlotDialog", "ggplot"))
        self.plotStyleBox.setItemText(4, _translate("configurationPlotDialog", "fivethirtyeight"))
        self.plotStyleBox.setItemText(5, _translate("configurationPlotDialog", "seaborn-v0_8"))
        self.label.setText(_translate("configurationPlotDialog", "Plot Style"))
        self.axisXInputTemp.setPlaceholderText(_translate("configurationPlotDialog", "Temperatura (F/C)"))
        self.label_3.setText(_translate("configurationPlotDialog", "X Axis Label"))
        self.label_4.setText(_translate("configurationPlotDialog", "Y Axis Label"))
        self.axisYInputTemp.setPlaceholderText(_translate("configurationPlotDialog", "TVDSS (m)"))
        self.fontsizeInputTemp.setPlaceholderText(_translate("configurationPlotDialog", "11, 12, ..."))
