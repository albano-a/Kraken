# Form implementation generated from reading ui file 'ui/plot_tendencia_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_plotTendenciaWindow(object):
    def setupUi(self, plotTendenciaWindow):
        plotTendenciaWindow.setObjectName("plotTendenciaWindow")
        plotTendenciaWindow.resize(668, 730)
        plotTendenciaWindow.setMinimumSize(QtCore.QSize(668, 720))
        plotTendenciaWindow.setMaximumSize(QtCore.QSize(668, 730))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        plotTendenciaWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=plotTendenciaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(parent=self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 631, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setMouseTracking(True)
        self.label_4.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.inputPressureUnit = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.inputPressureUnit.setObjectName("inputPressureUnit")
        self.gridLayout_3.addWidget(self.inputPressureUnit, 0, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_6.setMouseTracking(True)
        self.label_6.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_5.setMouseTracking(True)
        self.label_5.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.agrupamentoSpinBox = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.agrupamentoSpinBox.setMaximum(5)
        self.agrupamentoSpinBox.setProperty("value", 0)
        self.agrupamentoSpinBox.setObjectName("agrupamentoSpinBox")
        self.gridLayout_3.addWidget(self.agrupamentoSpinBox, 2, 1, 1, 2)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 2)
        self.cotaRadioBtnGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cotaRadioBtnGroupBox.setFont(font)
        self.cotaRadioBtnGroupBox.setStyleSheet("QGroupBox {\n"
"    background-color: #ededed;\n"
"}")
        self.cotaRadioBtnGroupBox.setObjectName("cotaRadioBtnGroupBox")
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.cotaRadioBtnGroupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(9, 21, 301, 100))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_18 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setMouseTracking(True)
        self.label_18.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_18.setObjectName("label_18")
        self.gridLayout_8.addWidget(self.label_18, 0, 0, 1, 1)
        self.cotaProfSim = QtWidgets.QRadioButton(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cotaProfSim.setFont(font)
        self.cotaProfSim.setObjectName("cotaProfSim")
        self.cotaButtonGroup = QtWidgets.QButtonGroup(plotTendenciaWindow)
        self.cotaButtonGroup.setObjectName("cotaButtonGroup")
        self.cotaButtonGroup.addButton(self.cotaProfSim)
        self.gridLayout_8.addWidget(self.cotaProfSim, 0, 1, 1, 1)
        self.cotaProfNao = QtWidgets.QRadioButton(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cotaProfNao.setFont(font)
        self.cotaProfNao.setObjectName("cotaProfNao")
        self.cotaButtonGroup.addButton(self.cotaProfNao)
        self.gridLayout_8.addWidget(self.cotaProfNao, 0, 2, 1, 1)
        self.labelMesaRotativa = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.labelMesaRotativa.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelMesaRotativa.setFont(font)
        self.labelMesaRotativa.setMouseTracking(True)
        self.labelMesaRotativa.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.labelMesaRotativa.setObjectName("labelMesaRotativa")
        self.gridLayout_8.addWidget(self.labelMesaRotativa, 1, 0, 1, 1)
        self.inputMesaRotativa = QtWidgets.QLineEdit(parent=self.layoutWidget_2)
        self.inputMesaRotativa.setEnabled(False)
        self.inputMesaRotativa.setObjectName("inputMesaRotativa")
        self.gridLayout_8.addWidget(self.inputMesaRotativa, 1, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setMouseTracking(True)
        self.label_19.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_19.setObjectName("label_19")
        self.gridLayout_8.addWidget(self.label_19, 2, 0, 1, 1)
        self.headerSim = QtWidgets.QRadioButton(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.headerSim.setFont(font)
        self.headerSim.setObjectName("headerSim")
        self.headerButtonGroup = QtWidgets.QButtonGroup(plotTendenciaWindow)
        self.headerButtonGroup.setObjectName("headerButtonGroup")
        self.headerButtonGroup.addButton(self.headerSim)
        self.gridLayout_8.addWidget(self.headerSim, 2, 1, 1, 1)
        self.headerNao = QtWidgets.QRadioButton(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.headerNao.setFont(font)
        self.headerNao.setObjectName("headerNao")
        self.headerButtonGroup.addButton(self.headerNao)
        self.gridLayout_8.addWidget(self.headerNao, 2, 2, 1, 1)
        self.labelHeaderLines = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.labelHeaderLines.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelHeaderLines.setFont(font)
        self.labelHeaderLines.setMouseTracking(True)
        self.labelHeaderLines.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.labelHeaderLines.setObjectName("labelHeaderLines")
        self.gridLayout_8.addWidget(self.labelHeaderLines, 3, 0, 1, 1)
        self.inputHeaderLines = QtWidgets.QLineEdit(parent=self.layoutWidget_2)
        self.inputHeaderLines.setEnabled(False)
        self.inputHeaderLines.setObjectName("inputHeaderLines")
        self.gridLayout_8.addWidget(self.inputHeaderLines, 3, 1, 1, 2)
        self.gridLayout.addWidget(self.cotaRadioBtnGroupBox, 1, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 132))
        self.groupBox_5.setStyleSheet("QGroupBox {\n"
"    background-color: #ededed;\n"
"}")
        self.groupBox_5.setObjectName("groupBox_5")
        self.layoutWidget_4 = QtWidgets.QWidget(parent=self.groupBox_5)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 20, 631, 101))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.layoutWidget_4)
        self.groupBox_8.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox_8.setObjectName("groupBox_8")
        self.layoutWidget_5 = QtWidgets.QWidget(parent=self.groupBox_8)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 20, 231, 71))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_11 = QtWidgets.QLabel(parent=self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.inputProfMin = QtWidgets.QLineEdit(parent=self.layoutWidget_5)
        self.inputProfMin.setObjectName("inputProfMin")
        self.gridLayout_6.addWidget(self.inputProfMin, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.inputProfMax = QtWidgets.QLineEdit(parent=self.layoutWidget_5)
        self.inputProfMax.setObjectName("inputProfMax")
        self.gridLayout_6.addWidget(self.inputProfMax, 1, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(parent=self.layoutWidget_4)
        self.groupBox_9.setObjectName("groupBox_9")
        self.layoutWidget_6 = QtWidgets.QWidget(parent=self.groupBox_9)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 20, 360, 74))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget_6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_14 = QtWidgets.QLabel(parent=self.layoutWidget_6)
        self.label_14.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 2, 0, 1, 1)
        self.inputPlotYAxis = QtWidgets.QLineEdit(parent=self.layoutWidget_6)
        self.inputPlotYAxis.setObjectName("inputPlotYAxis")
        self.gridLayout_7.addWidget(self.inputPlotYAxis, 2, 1, 1, 4)
        self.label_16 = QtWidgets.QLabel(parent=self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 0, 0, 1, 1)
        self.inputPlotXAxis = QtWidgets.QLineEdit(parent=self.layoutWidget_6)
        self.inputPlotXAxis.setObjectName("inputPlotXAxis")
        self.gridLayout_7.addWidget(self.inputPlotXAxis, 1, 1, 1, 4)
        self.inputPlotTitle = QtWidgets.QLineEdit(parent=self.layoutWidget_6)
        self.inputPlotTitle.setMaximumSize(QtCore.QSize(150, 16777215))
        self.inputPlotTitle.setObjectName("inputPlotTitle")
        self.gridLayout_7.addWidget(self.inputPlotTitle, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(parent=self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 1, 0, 1, 1)
        self.lineColorComboBox = QtWidgets.QComboBox(parent=self.layoutWidget_6)
        self.lineColorComboBox.setEnabled(False)
        self.lineColorComboBox.setObjectName("lineColorComboBox")
        self.gridLayout_7.addWidget(self.lineColorComboBox, 0, 3, 1, 2)
        self.horizontalLayout_2.addWidget(self.groupBox_9)
        self.gridLayout.addWidget(self.groupBox_5, 3, 0, 1, 2)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        self.selectFileGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.selectFileGroupBox.setMinimumSize(QtCore.QSize(0, 130))
        self.selectFileGroupBox.setMaximumSize(QtCore.QSize(16777215, 152))
        self.selectFileGroupBox.setStyleSheet("QGroupBox {\n"
"    background-color: #ededed;\n"
"}")
        self.selectFileGroupBox.setFlat(False)
        self.selectFileGroupBox.setCheckable(False)
        self.selectFileGroupBox.setObjectName("selectFileGroupBox")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.selectFileGroupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 291, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(True)
        self.label_3.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.txtRadioButton = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtRadioButton.setFont(font)
        self.txtRadioButton.setObjectName("txtRadioButton")
        self.fileButtonGroup = QtWidgets.QButtonGroup(plotTendenciaWindow)
        self.fileButtonGroup.setObjectName("fileButtonGroup")
        self.fileButtonGroup.addButton(self.txtRadioButton)
        self.gridLayout_2.addWidget(self.txtRadioButton, 1, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.xlsxRadioButton = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        self.xlsxRadioButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.xlsxRadioButton.setFont(font)
        self.xlsxRadioButton.setObjectName("xlsxRadioButton")
        self.fileButtonGroup.addButton(self.xlsxRadioButton)
        self.gridLayout_2.addWidget(self.xlsxRadioButton, 1, 3, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_2.setMouseTracking(True)
        self.label_2.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.selectFileComboBox = QtWidgets.QComboBox(parent=self.layoutWidget1)
        self.selectFileComboBox.setObjectName("selectFileComboBox")
        self.gridLayout_2.addWidget(self.selectFileComboBox, 0, 1, 1, 3)
        self.csvRadioButton = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.csvRadioButton.setFont(font)
        self.csvRadioButton.setObjectName("csvRadioButton")
        self.fileButtonGroup.addButton(self.csvRadioButton)
        self.gridLayout_2.addWidget(self.csvRadioButton, 1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setMouseTracking(True)
        self.label_12.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 4)
        self.gridLayout.addWidget(self.selectFileGroupBox, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(100, 50))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tendenciaPlotBtn = QtWidgets.QPushButton(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tendenciaPlotBtn.sizePolicy().hasHeightForWidth())
        self.tendenciaPlotBtn.setSizePolicy(sizePolicy)
        self.tendenciaPlotBtn.setMinimumSize(QtCore.QSize(200, 25))
        self.tendenciaPlotBtn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tendenciaPlotBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")
        self.tendenciaPlotBtn.setObjectName("tendenciaPlotBtn")
        self.horizontalLayout.addWidget(self.tendenciaPlotBtn)
        self.gridLayout.addWidget(self.frame_4, 4, 0, 1, 2)
        self.outputAfterPlotted = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.outputAfterPlotted.setMaximumSize(QtCore.QSize(16777215, 50))
        self.outputAfterPlotted.setWhatsThis("")
        self.outputAfterPlotted.setObjectName("outputAfterPlotted")
        self.gridLayout.addWidget(self.outputAfterPlotted, 5, 0, 1, 2)
        plotTendenciaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=plotTendenciaWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        plotTendenciaWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=plotTendenciaWindow)
        self.statusbar.setObjectName("statusbar")
        plotTendenciaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(plotTendenciaWindow)
        QtCore.QMetaObject.connectSlotsByName(plotTendenciaWindow)
        plotTendenciaWindow.setTabOrder(self.selectFileComboBox, self.csvRadioButton)
        plotTendenciaWindow.setTabOrder(self.csvRadioButton, self.txtRadioButton)
        plotTendenciaWindow.setTabOrder(self.txtRadioButton, self.xlsxRadioButton)
        plotTendenciaWindow.setTabOrder(self.xlsxRadioButton, self.cotaProfSim)
        plotTendenciaWindow.setTabOrder(self.cotaProfSim, self.cotaProfNao)
        plotTendenciaWindow.setTabOrder(self.cotaProfNao, self.inputMesaRotativa)
        plotTendenciaWindow.setTabOrder(self.inputMesaRotativa, self.headerSim)
        plotTendenciaWindow.setTabOrder(self.headerSim, self.headerNao)
        plotTendenciaWindow.setTabOrder(self.headerNao, self.inputHeaderLines)
        plotTendenciaWindow.setTabOrder(self.inputHeaderLines, self.inputPressureUnit)
        plotTendenciaWindow.setTabOrder(self.inputPressureUnit, self.agrupamentoSpinBox)
        plotTendenciaWindow.setTabOrder(self.agrupamentoSpinBox, self.inputProfMin)
        plotTendenciaWindow.setTabOrder(self.inputProfMin, self.inputProfMax)
        plotTendenciaWindow.setTabOrder(self.inputProfMax, self.inputPlotTitle)
        plotTendenciaWindow.setTabOrder(self.inputPlotTitle, self.inputPlotXAxis)
        plotTendenciaWindow.setTabOrder(self.inputPlotXAxis, self.inputPlotYAxis)
        plotTendenciaWindow.setTabOrder(self.inputPlotYAxis, self.lineColorComboBox)
        plotTendenciaWindow.setTabOrder(self.lineColorComboBox, self.tendenciaPlotBtn)
        plotTendenciaWindow.setTabOrder(self.tendenciaPlotBtn, self.outputAfterPlotted)

    def retranslateUi(self, plotTendenciaWindow):
        _translate = QtCore.QCoreApplication.translate
        plotTendenciaWindow.setWindowTitle(_translate("plotTendenciaWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("plotTendenciaWindow", "Configurações das Linhas de Têndencia"))
        self.label_4.setText(_translate("plotTendenciaWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Unidade de Pressão*:</span></p></body></html>"))
        self.inputPressureUnit.setToolTip(_translate("plotTendenciaWindow", "A unidade de pressão dos dados carregados."))
        self.label_6.setText(_translate("plotTendenciaWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Para se realizada o plot das linhas de tendência, é necessário dividir <br/>o dado em agrupamentos, sendo o padrão dividir em 2 agrupamentos.</span></p></body></html>"))
        self.label_5.setText(_translate("plotTendenciaWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Agrupamento (cluster) dos dados*:</span></p></body></html>"))
        self.agrupamentoSpinBox.setToolTip(_translate("plotTendenciaWindow", "Agrupamentos (Cluster) dos dados."))
        self.cotaRadioBtnGroupBox.setTitle(_translate("plotTendenciaWindow", "Configurações dos dados"))
        self.label_18.setStatusTip(_translate("plotTendenciaWindow", "Profundidade em cota é igual a mesa rotativa menos a profundidade medida."))
        self.label_18.setText(_translate("plotTendenciaWindow", "<html><head/><body><p align=\"right\">Profundidade em cota?*:</p></body></html>"))
        self.cotaProfSim.setText(_translate("plotTendenciaWindow", "Sim"))
        self.cotaProfNao.setText(_translate("plotTendenciaWindow", "Não"))
        self.labelMesaRotativa.setStatusTip(_translate("plotTendenciaWindow", "Mesa rotativa é a altura da plataforma até a superfície do mar/superfície terrestre."))
        self.labelMesaRotativa.setText(_translate("plotTendenciaWindow", "<html><head/><body><p align=\"right\">Mesa Rotativa*:</p></body></html>"))
        self.label_19.setStatusTip(_translate("plotTendenciaWindow", "Se o arquivo possui cabeçalho. Comum em arquivos las e csv."))
        self.label_19.setText(_translate("plotTendenciaWindow", "<html><head/><body><p align=\"right\">Cabeçalho?*:</p></body></html>"))
        self.headerSim.setText(_translate("plotTendenciaWindow", "Sim"))
        self.headerNao.setText(_translate("plotTendenciaWindow", "Não"))
        self.labelHeaderLines.setStatusTip(_translate("plotTendenciaWindow", "Se houver cabeçalho, quantas linhas pular?"))
        self.labelHeaderLines.setText(_translate("plotTendenciaWindow", "<html><head/><body><p align=\"right\">Quantas linhas?*:</p></body></html>"))
        self.groupBox_5.setTitle(_translate("plotTendenciaWindow", "Configurações do Gráfico"))
        self.groupBox_8.setTitle(_translate("plotTendenciaWindow", "Limitar a Profundidade"))
        self.label_11.setText(_translate("plotTendenciaWindow", "Profundidade Mínima:"))
        self.label_13.setText(_translate("plotTendenciaWindow", "Profundidade Máxima:"))
        self.groupBox_9.setTitle(_translate("plotTendenciaWindow", "Título e eixos do gráfico"))
        self.label_14.setText(_translate("plotTendenciaWindow", "Cor da Linha"))
        self.label_15.setText(_translate("plotTendenciaWindow", "Eixo y:"))
        self.label_16.setText(_translate("plotTendenciaWindow", "Título:"))
        self.label_17.setText(_translate("plotTendenciaWindow", "Eixo x:"))
        self.label.setText(_translate("plotTendenciaWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:696;\">Determinação do contato de fluidos</span></p><p><span style=\" font-size:10pt;\">Para determinação do contato entre os fluidos, usou-se de aprendizado de máquina para fazer a divisão dos dados, e também utilizou-se das pressões de fluido para análise parcial dos tipos de fluidos.</span></p></body></html>"))
        self.selectFileGroupBox.setTitle(_translate("plotTendenciaWindow", "Arquivo"))
        self.label_3.setText(_translate("plotTendenciaWindow", "<html><head/><body><p align=\"right\">Tipo de arquivo:</p></body></html>"))
        self.txtRadioButton.setToolTip(_translate("plotTendenciaWindow", "<html><head/><body><p>Arquivos de texto no geral. Lembre-se que nesse caso, os valores devem ser separados por tabulação (tab)</p></body></html>"))
        self.txtRadioButton.setText(_translate("plotTendenciaWindow", "txt"))
        self.xlsxRadioButton.setToolTip(_translate("plotTendenciaWindow", "<html><head/><body><p>Um arquivo .xlsx é uma planilha eletrônica, como no Excel.</p></body></html>"))
        self.xlsxRadioButton.setText(_translate("plotTendenciaWindow", "xlsx"))
        self.label_2.setText(_translate("plotTendenciaWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Selecione o arquivo:</span></p></body></html>"))
        self.csvRadioButton.setToolTip(_translate("plotTendenciaWindow", "<html><head/><body><p>Arquivos <span style=\" font-weight:700;\">C</span>omma <span style=\" font-weight:700;\">S</span>eparated <span style=\" font-weight:700;\">V</span>alues (valores separados por vírgula) são arquivos comumente utilizados para armazenamento de dados.</p></body></html>"))
        self.csvRadioButton.setText(_translate("plotTendenciaWindow", "csv"))
        self.label_12.setText(_translate("plotTendenciaWindow", "<html><head/><body><p align=\"center\">Arquivos aceitos até agora são o .csv e .txt. <br/>Futuramente há a pretensão de colocar <br> suporte a arquivos .xlsx</p></body></html>"))
        self.tendenciaPlotBtn.setText(_translate("plotTendenciaWindow", "Plotar"))
        self.outputAfterPlotted.setStatusTip(_translate("plotTendenciaWindow", "A profundidade do contato entre os fluidos aparecerá nessa área após o plot."))
        self.outputAfterPlotted.setHtml(_translate("plotTendenciaWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.outputAfterPlotted.setPlaceholderText(_translate("plotTendenciaWindow", "A profundidade do contato entre os fluidos aparecerá nessa área após o plot."))
