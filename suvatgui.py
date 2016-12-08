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
        suvat.resize(1090, 626)
        self.centralWidget = QtWidgets.QWidget(suvat)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1091, 621))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 5)
        suvat.setCentralWidget(self.centralWidget)

        self.retranslateUi(suvat)
        QtCore.QMetaObject.connectSlotsByName(suvat)

    def retranslateUi(self, suvat):
        _translate = QtCore.QCoreApplication.translate
        suvat.setWindowTitle(_translate("suvat", "suvat"))
        self.pushButton.setText(_translate("suvat", "Goes back"))
        self.label_2.setText(_translate("suvat", "Projectile motion questions"))
        self.label.setText(_translate("suvat", "TextLabel"))

