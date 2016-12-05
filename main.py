import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qdarkstyle


class Window(QWidget):  # TODO: Make application in Qt Designer

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(900, 550)
        self.center()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        font = QFont("Times", 40, QFont.Bold)
        label = QLabel()
        label.setText("Physics Practice 1.0")
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)

        decayButton = QPushButton("Radioactive Decay", self)

        box = QVBoxLayout()
        box.addWidget(label)
        box.addStretch()
        box.addWidget(decayButton)
        box.addStretch()
        self.setLayout(box)

        self.setWindowTitle("Physics Practice")
        self.show()

    def center(self):

        windowGeometry = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(centerPoint)
        self.move(windowGeometry.topLeft())

    def closeEvent(self, event):
        message = QMessageBox.question(self, 'Message', "Are you sure you want to quit?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if message == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
