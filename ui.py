from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import test
import radioactivedecay
import suvat
import suvatgui

class mainApp(QtWidgets.QMainWindow, test.Ui_main):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton_2.clicked.connect(self.button2Clicked)

    def buttonClicked(self):
        self.hide()
        self.suvatApp = suvatApp(self)
        self.suvatApp.show()

    def button2Clicked(self):
        print("your nan")
        radioactivedecay.generate()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Alert', "Are you sure about that?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class suvatApp(QtWidgets.QMainWindow, suvatgui.Ui_suvat):
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)
        pixmap = QtGui.QPixmap("test.png")
        self.label.setPixmap(pixmap)

    def buttonClicked(self):
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
    main = mainApp()
    main.show()
    sys.exit(app.exec_())


def suvatRun():
    suvat = suvatApp()
    suvat.show()

if __name__ == '__main__':
    main()
