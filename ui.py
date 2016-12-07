from PyQt5 import QtGui, QtWidgets
import sys
import test
import radioactivedecay
import suvat
import suvatgui
import os


class MainApp(QtWidgets.QMainWindow, test.Ui_main):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)
        self.pushButton_2.clicked.connect(self.button2_clicked)
        self.suvatApp = SuvatApp(self)

    def button_clicked(self):
        self.hide()
        self.suvatApp.show()

    def button2_clicked(self):
        radioactivedecay.generate()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Alert', "Are you sure about that?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class SuvatApp(QtWidgets.QMainWindow, suvatgui.Ui_suvat):
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)
        suvat.generate()
        pixmap = QtGui.QPixmap("test.png")
        self.label.setPixmap(pixmap)
        os.remove('test.png')

    def button_clicked(self):
        self.close()
        self.parent().show()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Alert', "Are you sure about that?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainApp()
    main.show()
    sys.exit(app.exec_())


def suvat_run():
    suvat_app = SuvatApp()
    suvat_app.show()


if __name__ == '__main__':
    main()
