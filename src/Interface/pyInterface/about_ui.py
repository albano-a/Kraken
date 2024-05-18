# Form implementation generated from reading ui file 'src/Interface/about.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(405, 390)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutWindow.sizePolicy().hasHeightForWidth())
        AboutWindow.setSizePolicy(sizePolicy)
        AboutWindow.setMinimumSize(QtCore.QSize(357, 296))
        AboutWindow.setMaximumSize(QtCore.QSize(405, 390))
        AboutWindow.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("J:/Universidade/GIECAR/qt_kraken_conversion/about.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AboutWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=AboutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 231, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("src/Interface\\../icon.ico"))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 381, 191))
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.creditsLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.creditsLabel.setGeometry(QtCore.QRect(40, 80, 301, 101))
        self.creditsLabel.setObjectName("creditsLabel")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 321, 61))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 110, 182, 23))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.giecarBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.giecarBtn.setMinimumSize(QtCore.QSize(60, 20))
        self.giecarBtn.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.giecarBtn.setFont(font)
        self.giecarBtn.setObjectName("giecarBtn")
        self.horizontalLayout.addWidget(self.giecarBtn)
        self.githubBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.githubBtn.setMinimumSize(QtCore.QSize(60, 20))
        self.githubBtn.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.githubBtn.setFont(font)
        self.githubBtn.setObjectName("githubBtn")
        self.horizontalLayout.addWidget(self.githubBtn)
        self.layoutWidget.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        AboutWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AboutWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 26))
        self.menubar.setObjectName("menubar")
        AboutWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AboutWindow)
        self.statusbar.setObjectName("statusbar")
        AboutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "MainWindow"))
        self.label.setText(_translate("AboutWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">KrakeN Geophysics v0.4.2</span></p></body></html>"))
        self.groupBox.setTitle(_translate("AboutWindow", "GNU General Public License"))
        self.creditsLabel.setText(_translate("AboutWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Developed by André Albano</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">GIECAR - UFF</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">2024</span></p></body></html>"))
        self.label_4.setText(_translate("AboutWindow", "<html><head/><body><p align=\"justify\">This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or at your option any later version.</p></body></html>"))
        self.label_3.setText(_translate("AboutWindow", "Access:"))
        self.giecarBtn.setToolTip(_translate("AboutWindow", "Acessar o site do Grupo de Interpretação Exploratória e Caracterização de Reservatório"))
        self.giecarBtn.setText(_translate("AboutWindow", "GIECAR"))
        self.githubBtn.setToolTip(_translate("AboutWindow", "Acessar o GitHub do projeto"))
        self.githubBtn.setText(_translate("AboutWindow", "GitHub"))
