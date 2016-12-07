# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\TomEaton\Documents\suvat\suvat.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_suvat(object):
    def setupUi(self, suvat):
        suvat.setObjectName("suvat")
        suvat.resize(756, 354)
        self.centralWidget = QtWidgets.QWidget(suvat)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 751, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        suvat.setCentralWidget(self.centralWidget)

        self.retranslateUi(suvat)
        QtCore.QMetaObject.connectSlotsByName(suvat)

    def retranslateUi(self, suvat):
        _translate = QtCore.QCoreApplication.translate
        suvat.setWindowTitle(_translate("suvat", "suvat"))
        self.label.setText(_translate("suvat", "TextLabel"))
        self.pushButton.setText(_translate("suvat", "Goes back"))
