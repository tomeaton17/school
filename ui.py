from PyQt5 import QtGui, QtWidgets
import sys
import test
import radioactivedecay


class mainApp(QtWidgets.QMainWindow, test.Ui_main):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("test")
        radioactivedecay.generate()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = mainApp()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
