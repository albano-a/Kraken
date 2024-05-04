# Form implementation generated from reading ui file 'src/Interface/temperatureInterface.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1049, 762)
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.importFileToolBtn = QtWidgets.QToolButton(parent=self.centralwidget)
        self.importFileToolBtn.setObjectName("importFileToolBtn")
        self.gridLayout.addWidget(self.importFileToolBtn, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.minDepthInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.minDepthInput.setObjectName("minDepthInput")
        self.gridLayout.addWidget(self.minDepthInput, 0, 4, 1, 1)
        self.inputFilePath = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inputFilePath.setObjectName("inputFilePath")
        self.gridLayout.addWidget(self.inputFilePath, 0, 2, 1, 1)
        self.maxDepthInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.maxDepthInput.setObjectName("maxDepthInput")
        self.gridLayout.addWidget(self.maxDepthInput, 0, 5, 1, 1)
        self.configurationButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.configurationButton.setObjectName("configurationButton")
        self.gridLayout.addWidget(self.configurationButton, 0, 6, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.plotButtonTemp = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plotButtonTemp.setObjectName("plotButtonTemp")
        self.verticalLayout.addWidget(self.plotButtonTemp)
        self.plotFrame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotFrame.sizePolicy().hasHeightForWidth())
        self.plotFrame.setSizePolicy(sizePolicy)
        self.plotFrame.setStyleSheet("QFrame {\n"
"    border: 1px solid #212121;\n"
"background-color: #f9f9f9;\n"
"}")
        self.plotFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.plotFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.plotFrame.setObjectName("plotFrame")
        self.verticalLayout.addWidget(self.plotFrame)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.backwardPlotButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backwardPlotButton.setObjectName("backwardPlotButton")
        self.gridLayout_2.addWidget(self.backwardPlotButton, 0, 2, 1, 1)
        self.homePlotButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.homePlotButton.setObjectName("homePlotButton")
        self.gridLayout_2.addWidget(self.homePlotButton, 0, 0, 1, 1)
        self.configureSubplotsButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.configureSubplotsButton.setObjectName("configureSubplotsButton")
        self.gridLayout_2.addWidget(self.configureSubplotsButton, 1, 2, 1, 1)
        self.forwardPlotButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.forwardPlotButton.setObjectName("forwardPlotButton")
        self.gridLayout_2.addWidget(self.forwardPlotButton, 0, 1, 1, 1)
        self.panPlotButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.panPlotButton.setObjectName("panPlotButton")
        self.gridLayout_2.addWidget(self.panPlotButton, 1, 0, 1, 1)
        self.zoomPlotButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.zoomPlotButton.setObjectName("zoomPlotButton")
        self.gridLayout_2.addWidget(self.zoomPlotButton, 1, 1, 1, 1)
        self.editPlotButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.editPlotButton.setObjectName("editPlotButton")
        self.gridLayout_2.addWidget(self.editPlotButton, 0, 3, 1, 1)
        self.savePlotButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.savePlotButton.setObjectName("savePlotButton")
        self.gridLayout_2.addWidget(self.savePlotButton, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "Filename:"))
        self.importFileToolBtn.setText(_translate("mainWindow", "..."))
        self.label_2.setText(_translate("mainWindow", "Depth (Optional):"))
        self.minDepthInput.setPlaceholderText(_translate("mainWindow", "Min. Depth"))
        self.inputFilePath.setPlaceholderText(_translate("mainWindow", "Input file\'s path or import it..."))
        self.maxDepthInput.setPlaceholderText(_translate("mainWindow", "Max. Depth"))
        self.configurationButton.setText(_translate("mainWindow", "Config..."))
        self.plotButtonTemp.setText(_translate("mainWindow", "Plot"))
        self.backwardPlotButton.setText(_translate("mainWindow", "Backward"))
        self.homePlotButton.setText(_translate("mainWindow", "Home"))
        self.configureSubplotsButton.setText(_translate("mainWindow", "Configure Subplots"))
        self.forwardPlotButton.setText(_translate("mainWindow", "Forward"))
        self.panPlotButton.setText(_translate("mainWindow", "Pan"))
        self.zoomPlotButton.setText(_translate("mainWindow", "Zoom"))
        self.editPlotButton.setText(_translate("mainWindow", "Edit"))
        self.savePlotButton.setText(_translate("mainWindow", "Save"))
