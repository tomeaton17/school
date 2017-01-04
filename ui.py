import os
import sys

from PyQt5 import QtGui, QtWidgets

import mainui
import projectile
import projectilegui
import questionStore
import radioactivedecay


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


# noinspection PyTypeChecker,PyCallByClass,PyCallByClass
class SuvatApp(QtWidgets.QMainWindow, projectilegui.Ui_suvat):
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.randomised = questionStore.Randomized()
        self.pushButton.clicked.connect(self.button_clicked)
        self.pushButton_2.clicked.connect(self.submit)
        self.lineEdit.returnPressed.connect(self.submit)
        self.answer = ""
        self.generate_question()


    def button_clicked(self):
        self.close()
        self.parent().show()

    def submit(self):
        if str(self.answer) == str(self.lineEdit.text()):
            QtWidgets.QMessageBox.information(self, "Well done", "Congrats")
            self.lineEdit.setText("")
            self.generate_question()
        else:
            QtWidgets.QMessageBox.critical(self, "Incorrect", "Unlucky m8")
            self.lineEdit.setText("")

    def generate_question(self):
        string = str(questionStore.load("projectilemotionquestions", self.randomised))
        temp = self.randomised.format(string)
        test = self.randomised.get_answer()
        if (self.randomised.args['equation'] == 'findtheta'):
            temp = str(temp) + str(test.answer_max_height()) + " Find theta in degreees."
            self.answer = test.answer_theta()
        if (self.randomised.args['equation'] == 'findmaxheight'):
            self.answer = test.answer_max_height()
        if (self.randomised.args['equation'] == 'findxdistance'):
            temp = str(temp) + str(
                test.answer_max_height()) + ". How far does the ball travel before it hits the ground?"
            self.answer = test.answer_xdistance()
        self.label_3.setText(temp)

        pixmap = QtGui.QPixmap("smaller.png")
        self.label.setPixmap(pixmap)
        os.remove('test.png')
        os.remove('smaller.png')

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
