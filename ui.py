import os
import sys

from PyQt5 import QtGui, QtWidgets

import radioactivedecay
import projectile
import projectilegui
import mainui


class MainApp(QtWidgets.QMainWindow, mainui.Ui_main):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)
        self.pushButton_2.clicked.connect(self.button2_clicked)
        self.suvatApp = SuvatApp(self)

    def button_clicked(self):
        self.hide()
        self.suvatApp.show()

    @staticmethod
    def button2_clicked():
        radioactivedecay.generate()

    def closeEvent(self, event):
        # noinspection PyCallByClass,PyTypeChecker
        reply = QtWidgets.QMessageBox.question(self, 'Alert', "Are you sure about that?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class SuvatApp(QtWidgets.QMainWindow, projectilegui.Ui_suvat):
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)
        projectile.generate()
        pixmap = QtGui.QPixmap("smaller.png")
        self.label.setPixmap(pixmap)
        os.remove('test.png')
        os.remove('smaller.png')

    def button_clicked(self):
        self.close()
        self.parent().show()

    def closeEvent(self, event):
        # noinspection PyTypeChecker,PyCallByClass
        reply = QtWidgets.QMessageBox.question(self, 'Alert', "Are you sure about that?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainapp = MainApp()
    mainapp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
